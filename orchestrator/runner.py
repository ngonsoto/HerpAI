from orchestrator.pipeline_manager import PipelineManager

def main():
    try:
        pipeline = PipelineManager(virus_type="HSV-2")
        context = pipeline.run_pipeline()
        pipeline.export_results()
        print("\n=== Final Output ===")
        for key, value in context.items():
            print(f"{key.replace('_', ' ').title()} Output:", value)
    except Exception as e:
        print(f"[ERROR] Pipeline execution failed: {e}")

if __name__ == "__main__":
    main()
