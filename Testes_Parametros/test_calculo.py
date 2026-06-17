import pytest
from calcule_total import calcule_total

@pytest.mark.parametrize("preco", [10.00, 50.00, 100.00])
@pytest.mark.parametrize("taxa_de_desconto", [0, 0.1, 0.25])
@pytest.mark.parametrize("taxa_de_imposto", [0, 0.05, 0.1])

def test_calcule_total(preco, taxa_de_desconto, taxa_de_imposto):
    excepted_discont = preco * taxa_de_desconto
    excepted_tax = (preco - excepted_discont) * taxa_de_imposto
    excepted_total = (preco - excepted_discont + excepted_tax)

    assert round(excepted_total, 2) 