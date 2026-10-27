# Milestone 2

## Part 1: Large-file test and timing comparison

Milestone 1 and Milestone 2 applications were run from the `beautifulsoup`
repository root against the same file,
`../Test Files of Milestone1/large.html`. Output was redirected to `/dev/null`
so the large result sets would not fill the terminal. The times below are the
elapsed wall-clock times reported by `time` for one run of each program.

| Task | Milestone 1 (no `SoupStrainer`) | Milestone 2 (with `SoupStrainer`) |
|---|---:|---:|
| Task 2 | 1 minute 31.78 seconds | 42.006 seconds |
| Task 3 | 1 minute 23.60 seconds | 1 minute 14.58 seconds |
| Task 4 | 1 minute 51.19 seconds | 1 minute 40.37 seconds |

The 100 MB `large.html` file contains approximately 472,205 `<a>` tags and
944,410 tags with an `id` attribute, counted with Beautiful Soup. The `id`
count is about twice the link count, so Task 4 retains many matching tags
while Task 2 retains only `<a>` tags. This may help explain why Task 2 showed
a larger timing improvement in these runs; the timing results are approximate
and come from one run per program.

Task 3 uses `SoupStrainer(True)` because it needs to report every tag. Since
every tag is relevant to that task, this filter cannot reduce the set of tags
that must be parsed. These timings are from single runs and should be treated
as approximate; system load and other run-to-run conditions can affect them.

Milestone 1 commands:

```bash
time PYTHONPATH=. python3 "../Milestone-1/task2.py" "../Test Files of Milestone1/large.html" > /dev/null
time PYTHONPATH=. python3 "../Milestone-1/task3.py" "../Test Files of Milestone1/large.html" > /dev/null
time PYTHONPATH=. python3 "../Milestone-1/task4.py" "../Test Files of Milestone1/large.html" > /dev/null
```

Milestone 2 commands:

```bash
time PYTHONPATH=. python3 apps/m2/task2.py "../Test Files of Milestone1/large.html" > /dev/null
time PYTHONPATH=. python3 apps/m2/task3.py "../Test Files of Milestone1/large.html" > /dev/null
time PYTHONPATH=. python3 apps/m2/task4.py "../Test Files of Milestone1/large.html" > /dev/null
```

## Part 2: Beautiful Soup API definitions

The locations below refer to the original source before the Milestone 2 Part 3
changes. Line numbers are the definition or implementation starting lines.

| API used | Original source location | Used for |
|---|---|---|
| `BeautifulSoup.__init__` (including `parse_only`) | `bs4/__init__.py:209` | Constructing the parsed document in Milestone 1 and passing a parser or `SoupStrainer` in Milestone 2 |
| `SoupStrainer.__init__` | `bs4/filter.py:345` | Creating the filters for Milestone 2 Tasks 2, 3, and 4 |
| `PageElement.get_text` | `bs4/element.py:524` | Getting the course heading text and Task 8 link text |
| `PageElement.find_parent` | `bs4/element.py:992` | Finding the article containing a Lecture Notes link |
| `Tag.get` | `bs4/element.py:2160` | Getting a link's `href` attribute |
| `Tag.__setitem__` | `bs4/element.py:2223` | Setting `class="test"` in Milestone 1 Task 7 |
| `Tag.__repr__` | `bs4/element.py:2298` | Rendering tag objects as text when printed in Milestone 1 Tasks 2 and 4 and Milestone 2 Tasks 2 and 4 |
| `Tag.prettify` | `bs4/element.py:2601` | Formatting parsed or modified markup for output |
| `Tag.find` | `bs4/element.py:2684` | Finding the `h3` heading inside an article |
| `Tag.find_all` | `bs4/element.py:2715` | Finding links, tags, tags with IDs, and `<b>`/`<p>` tags |
| `Tag.select` | `bs4/element.py:2799` | Finding HTTPS links with a CSS selector |
| `Tag.name` attribute initialization | `bs4/element.py:1648` | Reading tag names in Milestone 2 Task 3 and replacing a tag name in Milestone 1 Task 6 |

## Part 3: SoupReplacer

`SoupReplacer(og_tag, alt_tag)` replaces matching tag names while Beautiful
Soup parses the document. For example, the Task 6 application uses
`SoupReplacer("b", "blockquote")` to replace `<b>` tags with `<blockquote>`
tags and writes the result to `outputB.html`.

Run the application from the repository root:

```bash
PYTHONPATH=. python3 apps/m2/task6.py "../Test Files of Milestone1/sample.html"
```

Two tests in `bs4/tests/test_soup.py` verify that matching tags are replaced
and other tag names are left unchanged.
