#!/usr/bin/env python3
"""
Q&A System for Dr. B.R. Ambedkar's Speech
Kalpit Pvt Ltd - AI Intern Hiring Assignment
"""

import os
import sys
import warnings
# Suppress all warnings
warnings.filterwarnings("ignore")

# Disable ChromaDB telemetry to remove those warning messages
os.environ['ANONYMIZED_TELEMETRY'] = 'False'

try:
    from langchain.document_loaders import TextLoader
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.vectorstores import Chroma
    from langchain.llms import Ollama
    from langchain.embeddings import OllamaEmbeddings
    from langchain.chains import RetrievalQA
    from langchain.prompts import PromptTemplate
    print("✅ All modules imported successfully")
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

class AmbedkarQASystem:
    def __init__(self, data_path="speech.txt", persist_directory="./chroma_db"):
        self.data_path = data_path
        self.persist_directory = persist_directory
        self.qa_chain = None
        self.vector_store = None
        
    def load_and_process_documents(self):
        """Load and split the document"""
        print("📖 Loading and processing Ambedkar's speech...")
        try:
            loader = TextLoader(self.data_path, encoding='utf-8')
            documents = loader.load()
            
            text_splitter = CharacterTextSplitter(
                chunk_size=500,  # Increased for better context
                chunk_overlap=100,
                separator="\n"
            )
            
            chunks = text_splitter.split_documents(documents)
            print(f"✅ Speech processed into {len(chunks)} meaningful chunks")
            return chunks
        except Exception as e:
            print(f"❌ Error loading document: {e}")
            return None
    
    def setup_system(self):
        """Setup the complete RAG system"""
        print("🔧 Initializing Q&A System...")
        
        try:
            # Use Ollama for embeddings (consistent with LLM)
            print("🔄 Loading embeddings model...")
            embeddings = OllamaEmbeddings(model="mistral")
            
            # Check if we already have a vector store
            if os.path.exists(self.persist_directory) and os.listdir(self.persist_directory):
                print("📚 Loading existing knowledge base...")
                self.vector_store = Chroma(
                    persist_directory=self.persist_directory,
                    embedding_function=embeddings
                )
            else:
                print("📝 Processing speech for the first time...")
                chunks = self.load_and_process_documents()
                if not chunks:
                    return False
                
                print("💾 Creating knowledge base...")
                self.vector_store = Chroma.from_documents(
                    documents=chunks,
                    embedding=embeddings,
                    persist_directory=self.persist_directory
                )
            
            # Setup the QA chain with Mistral
            print("🤖 Initializing Mistral 7B for answering...")
            llm = Ollama(model="mistral", temperature=0.1)
            
            # Improved prompt for better answers
            prompt_template = """You are an expert assistant analyzing Dr. B.R. Ambedkar's speech "Annihilation of Caste". 
Use the following excerpt from the speech to answer the question. Be precise and stay true to Ambedkar's ideas.

EXCERPT FROM SPEECH:
{context}

QUESTION: {question}

INSTRUCTIONS:
1. Answer based ONLY on the provided excerpt
2. If the excerpt doesn't contain relevant information, say so
3. Be concise and accurate
4. Focus on Ambedkar's key arguments

ANSWER:"""
            
            PROMPT = PromptTemplate(
                template=prompt_template, 
                input_variables=["context", "question"]
            )
            
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=self.vector_store.as_retriever(
                    search_type="similarity",
                    search_kwargs={"k": 1}  # Reduced to avoid the warning
                ),
                chain_type_kwargs={"prompt": PROMPT},
                return_source_documents=False
            )
            
            print("✅ AmbedkarGPT System Ready!")
            return True
            
        except Exception as e:
            print(f"❌ System setup failed: {e}")
            return False
    
    def ask_question(self, question):
        """Ask a question about Ambedkar's speech"""
        if not self.qa_chain:
            print("⚠️ Please initialize the system first")
            return
        
        print(f"\n🤔 Question: {question}")
        print("🔍 Analyzing Ambedkar's speech...")
        
        try:
            result = self.qa_chain({"query": question})
            print(f"\n💡 Answer: {result['result']}")
            print("\n" + "─" * 60)
        except Exception as e:
            print(f"❌ Error finding answer: {e}")

def check_ollama():
    """Check if Ollama is running with Mistral"""
    try:
        import subprocess
        print("🔍 Checking Ollama setup...")
        result = subprocess.run(
            ["ollama", "list"], 
            capture_output=True, 
            text=True, 
            shell=True,
            timeout=10
        )
        if "mistral" in result.stdout:
            print("✅ Mistral model available")
            return True
        else:
            print("❌ Mistral model not found. Please run: ollama pull mistral")
            return False
    except Exception as e:
        print(f"❌ Ollama not accessible: {e}")
        return False

def display_welcome():
    """Display welcome message and instructions"""
    print("=" * 70)
    print("🧠 AMBEDKAR GPT - Q&A System")
    print("Based on 'Annihilation of Caste' by Dr. B.R. Ambedkar")
    print("=" * 70)
    print("\nThis system answers questions based solely on Ambedkar's speech.")
    print("It uses Mistral 7B via Ollama and RAG technology.\n")

def display_example_questions():
    """Show example questions users can ask"""
    examples = [
        "What is the real remedy for caste according to Ambedkar?",
        "What does Ambedkar say about the shastras?",
        "How does Ambedkar compare social reform to gardening?",
        "What is the relationship between scriptures and caste practice?",
        "Why does Ambedkar say you cannot have both caste and disbelief in shastras?"
    ]
    
    print("💡 Example questions you can ask:")
    for i, question in enumerate(examples, 1):
        print(f"   {i}. {question}")
    print()

def main():
    """Main application loop"""
    display_welcome()
    
    # Check prerequisites
    if not os.path.exists("speech.txt"):
        print("❌ Error: speech.txt file not found in current directory")
        return
    
    if not check_ollama():
        return
    
    # Initialize system
    qa_system = AmbedkarQASystem()
    
    if not qa_system.setup_system():
        print("❌ Failed to initialize the Q&A system")
        return
    
    # Main interaction loop
    print("\n" + "=" * 70)
    print("💬 READY: You can now ask questions about Ambedkar's speech")
    print("Type 'quit' or 'exit' to end the session")
    print("=" * 70)
    
    display_example_questions()
    
    while True:
        try:
            question = input("\n🎯 Your question: ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                print("\n🙏 Thank you for exploring Ambedkar's ideas!")
                print("   'The real remedy is to destroy the belief in the sanctity of the shastras.'")
                break
                
            if not question:
                print("⚠️ Please enter a question")
                continue
                
            # Process the question
            qa_system.ask_question(question)
            
        except KeyboardInterrupt:
            print("\n\n👋 Session ended. Thank you!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()