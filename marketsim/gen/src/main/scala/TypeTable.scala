case class TypeTable() {

    var types : Map[String, Typed.Function] = Map.empty

    override def toString = types mkString "\r\n"

    def getOrElseUpdate(name : String, default : => Typed.Function) =
        types get name match {
            case Some(f) => f
            case None =>
                val f = default
                types = types updated (f.name, f)
                f
        }

    def contains(name : String) = types contains name

    def lookup(name : AST.QualifiedName) =
        types.get(name.toString) match {
            case Some(t) => t
            case _ => throw new Exception(s"cannot lookup type for $name")
        }
}
