import gradio as gr
from deal_agent_framework import DealAgentFramework
from agents.deals import Opportunity, Deal

class App:

    def __init__(self):    
        self.agent_framework = None

    def run(self):
        with gr.Blocks(title="SmartPrice AI: Multi-Agent System for Automated Deal Discovery", fill_width=True) as ui:
        
            def table_for(opps):
                return [[opp.deal.product_description, f"${opp.deal.price:.2f}", f"${opp.estimate:.2f}", f"${opp.discount:.2f}", opp.deal.url] for opp in opps]
        
            def start():
                self.agent_framework = DealAgentFramework()
                self.agent_framework.init_agents_as_needed()
                opportunities = self.agent_framework.memory
                table = table_for(opportunities)
                return table
        
            def go():
                self.agent_framework.run()
                new_opportunities = self.agent_framework.memory
                table = table_for(new_opportunities)
                return table
        
            def do_select(selected_index: gr.SelectData):
                opportunities = self.agent_framework.memory
                row = selected_index.index[0]
                opportunity = opportunities[row]
                self.agent_framework.planner.messenger.alert(opportunity)
        
            with gr.Row():
                gr.Markdown('<div style="text-align: center;font-size:24px">SmartPrice AI: Multi-Agent System for Automated Deal Discovery</div>')
            with gr.Row():
                gr.Markdown('<div style="text-align: center;font-size:14px">Autonomous agent framework for intelligent deal discovery, combining a fine-tuned LLM deployed on Modal with a frontier-driven RAG pipeline and Chroma vector store.</div>')
            with gr.Row():
                gr.Markdown('<div style="text-align: center;font-size:14px">Deals surfaced so far:</div>')
            with gr.Row():
                opportunities_dataframe = gr.Dataframe(
                    headers=["Description", "Price", "Estimate", "Discount", "URL"],
                    wrap=True,
                    column_widths=[4, 1, 1, 1, 2],
                    row_count=10,
                    col_count=5,
                    max_height=400,
                )
        
            ui.load(start, inputs=[], outputs=[opportunities_dataframe])

            timer = gr.Timer(value=60)
            timer.tick(go, inputs=[], outputs=[opportunities_dataframe])

            opportunities_dataframe.select(do_select)
        
        ui.launch(share=False, inbrowser=True)

if __name__=="__main__":
    App().run()
    