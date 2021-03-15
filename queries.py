conditions_query = """
{
  conditions{
		name
    text
    source
  }
}
"""

trait_query = """
{
	traits{
		name
    text
    source
  }
}
"""

spells_query = """
{
  spells{
    name
    actions
    level
    range
    area
    traits{name}
    traditions
    text
    savingthrow
    criticalfailure
    failure
    success
    criticalsuccess
    source
  }
}
"""

