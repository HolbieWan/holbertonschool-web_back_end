# Pagination

Pagination is a method to divide large datasets into smaller, manageable chunks to improve performance and user experience. It requires implied ordering (e.g., by unique identifiers or created dates) and can be implemented in various ways based on the application’s needs.

## How to paginate a dataset with simple page and page_size parameters
**What:**
+  Paginating a dataset involves dividing it into smaller chunks (pages) using page and page_size.

**Why:**
+ This helps manage large datasets by retrieving only a subset of data at a time.

**How:**
+ Calculate start and end indices based on page and page_size.

**Example:**
```python
def paginate(dataset, page, page_size):
    start = (page - 1) * page_size
    end = start + page_size
    return dataset[start:end]

data = [1, 2, 3, 4, 5, 6]
print(paginate(data, page=2, page_size=2))  # Output: [3, 4]
```

**Example_2:**

Suppose you have a dataset [A, B, C, D, E, F, G, H] and want to paginate it:
```
Page 1 (page=1, page_size=3):
start_index = (1 - 1) * 3 = 0
end_index = 0 + 3 = 3
Items: [A, B, C]

Page 2 (page=2, page_size=3):
start_index = (2 - 1) * 3 = 3
end_index = 3 + 3 = 6
Items: [D, E, F]
```

## How to paginate a dataset with hypermedia metadata
Paginate a Dataset with Hypermedia Metadata

**What:**
+ Hypermedia pagination includes metadata (e.g., total pages, next/previous links) along with the data.

**Why:**
+ Provides additional context for navigation.

**How:**
+ Include metadata fields in the response.

**Example:**
```python
def hypermedia_paginate(dataset, page, page_size):
    total_items = len(dataset)
    total_pages = (total_items + page_size - 1) // page_size
    start = (page - 1) * page_size
    end = start + page_size
    data = dataset[start:end]
    return {
        "data": data,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
        "has_next": page < total_pages
    }

data = [1, 2, 3, 4, 5, 6]
print(hypermedia_paginate(data, page=2, page_size=2))
# Output: {'data': [3, 4], 'page': 2, 'page_size': 2, 'total_pages': 3, 'has_next': True}
```

## How to paginate in a deletion-resilient manner

Paginate in a Deletion-Resilient Manner

**What:** 
+ Deletion-resilient pagination ensures consistent results despite deletions by using unique identifiers (e.g., item IDs).

**Why:** 
+ Index-based pagination can fail if items are deleted.

**How:** 
+ Use last_seen_id to fetch subsequent items.

**Example:**
```python
def deletion_resilient_paginate(dataset, last_seen_id=None, page_size=2):
    start_index = 0
    if last_seen_id:
        for index, item in enumerate(dataset):
            if item['id'] == last_seen_id:
                start_index = index + 1
                break
    return dataset[start_index:start_index + page_size]

data = [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}]
print(deletion_resilient_paginate(data, last_seen_id=2, page_size=2))
# Output: [{'id': 3}, {'id': 4}]
```

**Benefits:** Easy to implement, stateless, supports custom sorting.

**Downsides:** Performance drops with large offsets; inconsistent results when data changes (page drift).

## Offset Pagination

**What:** 
+ Use limit (number of items per page) and offset (starting point) to fetch data.

**When to Use:**
+ Simple cases with small datasets and no frequent updates.

**How:**
+ Add limit and offset parameters to your query.

**Example:**
```python
# SQL query for third page with 20 items per page
SELECT * FROM Items ORDER BY Id LIMIT 20 OFFSET 40;

# API request
GET /items?limit=20&offset=40
```

**Benefits:** Consistent ordering; performs well with large datasets.

**Downsides:** Coupled to filters; unsuitable for low-cardinality fields.

## Keyset Pagination

**What:** 
+ Use the last returned value (e.g., timestamp) as a filter for the next query.
**When to Use:** 
+ Time-series or data with natural high-cardinality keys.
**How:** 
+ Add filters like created:lte to fetch subsequent pages.

**Example:**
```python
# SQL query for items created before a specific timestamp
SELECT * FROM Items WHERE created <= '2021-01-20T00:00:00' ORDER BY Id LIMIT 20;

# API request
GET /items?limit=20&created:lte:2021-01-20T00:00:00
```

**Benefits:** Decouples pagination from filters; stable ordering even with updates.
**Downsides:** More complex backend implementation; invalid start_id if items are deleted.

## Sorting in APIs

**What:** Allows users to order results by specific fields (e.g., created, email).
**How:** Use a sort_by parameter paired with ascending/descending order.

**Example Formats:**
```python
GET /users?sort_by=-email (descending)
GET /users?sort_by=email&order_by=asc (ascending)
```

**Multi-Column Sorting Example:**
```sql
# SQL query for multi-column sorting
SELECT * FROM Items ORDER BY Last_Modified DESC, Email ASC LIMIT 20;

# API request
GET /users?sort_by=-last_modified,+email
```

### Tips:

+ Pair sorting fields and order to avoid ambiguity.
+ Preserve parameter order in caching and deserialization.