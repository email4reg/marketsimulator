@category = "Order"
package order
{
    @python.order.factory("order.market.Order_Impl")
    def Market(side = side.Sell(), volume = constant(1.)) : IObservable[Order]

    @python.order.factory("order.limit.Order_Impl")
    def Limit(side = side.Sell(), price = constant(100.), volume = constant(1.)) : IObservable[Order]

    @python.order.factory("order.meta.fixed_budget.Order_Impl")
    def FixedBudget(side = side.Sell(), budget = constant(1000.)) : IObservable[Order]

    @python.order.factory("order.meta.ioc.Order_Impl")
    def ImmediateOrCancel(proto = Limit()) : IObservable[Order]

    @python.order.factory("order.meta.stoploss.Order_Impl")
    def StopLoss(maxloss = const(0.1), proto = Market()) : IObservable[Order]
}