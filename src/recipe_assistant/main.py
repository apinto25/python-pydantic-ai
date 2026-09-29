from datetime import date
from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()
agent = Agent(
    "google:gemini-3.6-flash",
    instructions="Eres un asistente de cocina. Recomiendas recetas según los"
        "ingredientes que el usuario tiene disponibles. Sé breve y práctico."
)


@agent.instructions
def add_season() -> str:
    month = date.today().month
    if month == 12:
        return("Estamos en diciembre. Si es posible prioriza recetas navideñas"
               "o de fin de año y menciona en tu respuesta que la receta es de"
               "temporada.")
    return(f"Estamos en el mes {month}. Prioriza ingredientes de temporada"
           "cuando sea relevante, y meciona en tu respuesta que la receta es"
           "de temporada.")


def main() -> None:
    result = agent.run_sync("Qué puedo cocinar con arroz y pollo en esta época del año?")
    print(result.output)
