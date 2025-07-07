import os
import glob
from src.pipeline.orchestrator import PipelineOrchestrator
from src.monitoring.performance import simulate_retrieval_test, generate_report

def main():
    """
    Main function to run the document processing pipeline.
    """
    print("Starting Intelligent Document Chunking System...")

    orchestrator = PipelineOrchestrator()
    
    # Process all documents in the data/samples directory
    sample_docs_path = os.path.join("data", "samples", "*")
    document_files = glob.glob(sample_docs_path)

    if not document_files:
        print("No sample documents found. Please add some to the data/samples directory.")
        return

    for file_path in document_files:
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            orchestrator.process_document(file_path, content)

    # Get the final state of the vector store
    final_vector_store = orchestrator.vector_store
    
    # Run performance monitoring simulation
    simulate_retrieval_test(final_vector_store)
    
    # Generate a final report
    report_metrics = {
        "total_documents_processed": len(document_files),
        "total_chunks_created": orchestrator.get_vector_store_size(),
    }
    generate_report(report_metrics)

    print("\\nSystem processing complete.")

if __name__ == "__main__":
    main() 