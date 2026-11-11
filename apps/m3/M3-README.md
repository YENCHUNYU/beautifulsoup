# Milestone 3: SoupReplacer API

## Application

Run `PYTHONPATH=../../ python3 task7.py <filename>` from this directory (or
install the local Beautiful Soup package and run `python3 task7.py <filename>`).
It parses HTML with `html.parser` and XML with the XML parser, sets
`class="test"` on every `<p>` tag as the tag is parsed, and writes the result
to `outputClass.html`. The update uses `SoupReplacer(xformer=...)`, rather than
walking the completed tree.

## Technical brief: Milestone 2 and Milestone 3

Milestone 2's `SoupReplacer(og_tag, alt_tag)` is a focused, easy-to-understand
convenience API: it expresses one common operation—renaming a tag—and keeps
the parsing callback contract hidden. Its limitation is that each new kind of
transformation would otherwise need another special constructor option or a
post-parse tree walk.

Milestone 3 keeps that pair-based interface for compatibility and adds
`name_xformer`, `attrs_xformer`, and `xformer` callbacks. The first two return
replacement values; `xformer` supports in-place mutations and other side
effects. This is more expressive, including transformations based on the
current tag's attributes, but it exposes more complexity: callbacks run during
parsing, so their order and the parser's evolving tag state matter, and callback
exceptions interrupt parsing.

I recommend keeping the Milestone 2 form as a simple convenience while
offering the callback form as an additive advanced API. Document a stable
execution order (name, attributes, then in-place callback), make callback
failures visible, and test the behavior across supported builders. For larger
or reusable transformation pipelines, a dedicated parse-event/plugin
abstraction may eventually be clearer than continuing to add callback
parameters to `SoupReplacer`. For the current use cases, the additive API is
the smallest extension that enables powerful parse-time changes without
breaking existing callers.
