# JSON Extraction Tool (JET)

Array selection:

Automatically groups by `item[*]`:
```
kind
items[*].volumeInfo.title
items[*].searchInfo.textSnippet
```

Explicitly group by `item[*]`:
```
kind
items[*](volumeInfo.title searchInfo.textSnippet)
```

## Query filter grammar

```
filter              ::= expression operator value_or_expression
value_or_expression ::= value | expression
value               ::= string | number | boolean | "null" | array | object     # parse as JSON
operator            ::= "=" | ">" | ">=" | "<" | "<="
```

### Expression Examples

'



