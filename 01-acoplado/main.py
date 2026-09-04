from mini_orion import Cliente, Carrinho, ItemCarrinho, ServicoCheckout

cliente1 = Cliente(nome="João", email="joao@example.com", cartao="1234-5678-9012-3456")
carrinho_cliente1 = Carrinho(
    itens=[
        ItemCarrinho(
            sku="SKU123",
            quantidade=2,
            preco_unitario=100.0,
        ),
        ItemCarrinho(
            sku="SKU456",
            quantidade=1,
            preco_unitario=150.0,
        ),
    ],
)

print(
    "Valor total do carrinho:",
    sum(item.quantidade * item.preco_unitario for item in carrinho_cliente1.itens),
)

checkout = ServicoCheckout()
resultado = checkout.fechar_pedido(
    carrinho_cliente1, cliente1
)

print("Resultado:", resultado)
