import sglang as sgl
import os
import json

def setup_backend():
    """Setup using OpenAI API"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Please set OPENAI_API_KEY environment variable")
        return False
    
    try:
        sgl.set_default_backend(sgl.OpenAI("gpt-3.5-turbo"))
        return True
    except Exception as e:
        print(f"Backend setup failed: {e}")
        return False

@sgl.function
def summarize_paper_simple(s, paper_text: str):
    """Paper summarization function"""

    s += sgl.system("You are an expert research assistant specializing in academic paper analysis.")
    
    s += sgl.user(f"""
    Please analyze this research paper and provide a structured summary:
    
    {paper_text}
    
    Create a summary with these sections:
    1. Main Research Question
    2. Methodology Used  
    3. Key Findings
    4. Significance/Impact
    5. Limitations
    
    Keep each section concise (2-3 sentences) and use academic language.
    """)
    
    s += sgl.assistant(sgl.gen("summary", max_tokens=500))

def main():
    
    if not setup_backend():
        return
    
    with open("sample_paper.txt", "r") as f:
        sample_paper = f.read()
    
    print("Analyzing sample paper...")
    
    try:
        result = summarize_paper_simple(sample_paper)

        print("\nSummary Results:")
        print("=" * 50)
        print(result["summary"])
        
        with open("paper_summary.txt", "w") as f:
            f.write("Research Paper Summary\n")
            f.write("=" * 50 + "\n\n")
            f.write(result["summary"])
        
        print(f"\nSummary saved to paper_summary.txt")
        
    except Exception as e:
        print(f"Analysis failed: {e}")

if __name__ == "__main__":
    main()