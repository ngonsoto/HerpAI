from agents.base_agent import BaseAgent
from jinja2 import Environment, FileSystemLoader

class ReportGeneratorAgent(BaseAgent):
    def __init__(self, context=None, variables=None):
        super().__init__(agent_name="report_generator", context=context, variables=variables)
        self.output_path = "output/final_report.md"
        self.template_file = "report_template.md"

    def _generate_report(self):
        try:
            env = Environment(loader=FileSystemLoader("templates"))
            template = env.get_template(self.template_file)

            report_text = template.render(
                context=self.context,
                virus_type=self.variables.get("virus_type", "Unknown")
            )

            with open(self.output_path, "w") as f:
                f.write(report_text)

            print(f"[ReportGenerator] Report written to: {self.output_path}")
            self.raw_output = {"report_path": self.output_path}
        except Exception as e:
            print(f"[ReportGenerator] Failed to generate report: {e}")
            self.raw_output = {"error": str(e)}

    def run(self):
        self._generate_report()
        
    def get_json(self):
        return {"report_path": self.output_path}
