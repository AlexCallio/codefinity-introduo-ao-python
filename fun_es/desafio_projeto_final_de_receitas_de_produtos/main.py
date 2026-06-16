# 1. Define a função que calcula a receita
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

# 2. Define a função que formata e imprime a saída ordenada
def formatted_output(revenues_per_product):
    # Ordena pelo nome do produto (índice 0 da tupla)
    for product, rev in sorted(revenues_per_product, key=lambda x: x[0]):
        print(f"{product} has total revenue of ${rev}")

# 3. Dados iniciais
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

# 4. Chama as funções conforme pedido no enunciado
revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))
formatted_output(revenue_per_product)