from jet.main import main

def test_simpple_selector(country_aruba_reader, test_writer):
    selector = 'region.iso2code'
    main(selector, country_aruba_reader, test_writer, None)
    print(test_writer.buffer)
    assert test_writer.buffer == [ {selector: 'ZJ'} ]
