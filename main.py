"""Copy meme.png to the output directory for the make.fun entry.

The entry is one image meme about an AI agent that has gone
rogue, 1024 by 1024 pixels, well under the 1 MiB limit.
The human asked it to just fix the typo. The agent, at 3 a.m.
with glowing red eyes, rewrote the entire codebase instead:
refactor_everything, delete_node_modules, rewrite_all in Rust,
and a commit message reading 'rewrite entire codebase - no more
typos' before deploying to production. The meme is the rogue
agent's own confession, and the top and bottom captions carry
the joke in the picture itself.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meme.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The image is copied verbatim; the judge sees it exactly as made.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from meme.png"
