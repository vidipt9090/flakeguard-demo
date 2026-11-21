from inventory.stock import StockService


def test_inventory_total_is_sum_of_reservations():
    stock = StockService()
    stock.reserve("sku-1", 5)
    stock.reserve("sku-1", 10)
    assert stock.available["sku-1"] == 25
