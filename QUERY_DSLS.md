# Query DSL comparison

JSON path limitations:

* Extraction of a single property.
* Filtering is tied to extraction.
* Querying on multiple properties may be possible but is hard to work with.





## Querying

### MongoDB

Simple matchers:

```js
// Equality:
{ "status": "A" }

// Less than:
{ "size": { "$lt": 30 } }

// Containment:
{ "status": { "$in": ["A", "B"] } }

// Regex
{ "item": /^p/ }

// Nested queries
{
    size: {
        h: 14
    }
}
// or this:
{
    "size.h": 14
}

```

Boolean matchers:

```js
// AND condition
{
    "status": "A",
    "qty": { "$lt": 30 }
}

// OR condition
{
    $or: [
        { status: "A" },
        { qty: { $lt: 30 } }
    ]
}

// AND + OR
{
    status: "A",
    $or: [
        { qty: { $lt: 30 } },
        { item: /^p/ }
    ]
}
```

Array matchers:
```js

// Multiple conditions on any element. Matches either of the following:
// { "size": [17] }
// { "size": [50, 11] }
{ size: { $gt: 15, $lt: 20 } }

// Multiple conditions on the same element
{ size: { $elemMatch: { $gt: 22, $lt: 30 } } }

// Query element in a specific position
{ "size.1": { $gt: 25 } }
```

## Scalar matches

* in
* not in


## Array matchers

```json
[
    {
        "id": 1,
        "item": "T-shirt",
        "colors": ["white", "black", "red"],
        "sizes": ["S", "M", "L", "XXL"]
    },
    {
        "id": 2,
        "item": "Sweat shirt",
        "colors": ["white", "teal"],
        "sizes": ["L", "XL", "XXL"]
    }
]
```

Primary array filters:

* Equals: `colors == ["teal"]` matches #2.
* Contains: `colors contains "white"` matches all.
* Subset:
* Size:


Derived array filters:
* Is empty: `colors == []` matches none.
* Not empty: `colors != []` matches all.


Notes:

* ❓: untested expression.
* 🐻: JSONPath extension from [https://support.smartbear.com/alertsite/docs/monitors/api/endpoint/jsonpath.html](Smartbear)


<table>
    <thead>
        <tr>
            <th>Condition</th>
            <th>JSON Path</th>
            <th>MongoDB</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Exact match<br>(matches ["red", "blank"] exactly)</td>
            <td>?(@.tags==['red','blank']) ❓</td>
            <td>{ tags: ["red", "blank"] }</td>
        </tr>
        <tr>
            <td>Array contains an element</td>
            <td>?(@.tags==['red','blank']) ❓</td>
            <td>{ tags: "red" ] }</td>
        </tr>
        <tr>
            <td>All matcher<br>(regardless of order or other elements)</td>
            <td>🐻</td>
            <td>{ tags: { $all: ["red", "blank"] } }</td>
        </tr>
        <tr>
            <td>// Single element matchers</td>
            <td>tags[?(@ == 'red')]<br>size[</td>
            <td>{ tags: "red" }<br>{ size: { $gt: 25 } }</td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>
