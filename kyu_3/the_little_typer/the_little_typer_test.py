from the_little_typer import parse_context


def test_parse_context():
    # Returns empty dict when passed an empty str
    assert parse_context("") == {}
    input_str = """
                myValue : A
                concat : List -> List -> List
                append : List -> A -> List
                map : (A -> B) -> (List -> List)
                
                pure : A -> List
                """
    output = parse_context(input_str)
    # Returns a dict with as many entries as there are non-empty lines in the input str
    assert len(output) == 5
    # output dict's keys match types defined in context
    assert list(output.keys()) == ['myValue', 'concat', 'append', 'map', 'pure']
