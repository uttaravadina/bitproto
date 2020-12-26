"""
bitproto.renderer_base
~~~~~~~~~~~~~~~~~~~~~~~

Renderer base class and utils.
"""

import os
from typing import Dict, List, Optional, Type as T

from bitproto.ast import Proto
from bitproto.errors import UnsupportedLanguageToRender

RendererClass = T["Renderer"]


def get_renderer_registry() -> Dict[str, RendererClass]:
    from bitproto.renderer_c import RendererC
    from bitproto.renderer_go import RendererGo
    from bitproto.renderer_py import RendererPy

    return {
        "c": RendererC,
        "go": RendererGo,
        "py": RendererPy,
    }


def get_renderer_cls(lang: str) -> Optional[RendererClass]:
    """Get renderer class by language.

        >>> get_renderer_cls("c")
        <class 'RendererC'>
    """
    registry = get_renderer_registry()
    return registry.get(lang, None)


class Renderer:
    """Base renderer class.

    :param proto: The parsed bitproto instance.
    :param outdir: The directory to write files, defaults to the source
       bitproto's file directory, or cwd.
    """

    def __init__(self, proto: Proto, outdir: Optional[str] = None) -> None:
        if outdir is None:
            if proto.filepath:  # Parsing from a file
                outdir = os.path.dirname(os.path.abspath(proto.filepath))
            else:  # Parsing from a memory string.
                outdir = os.getcwd()
        self.proto = proto
        self.outdir = outdir

    def format_out_filepath(self, extension: str) -> str:
        """Returns the output file's path for given extension.

            >>> format_out_filepath(".go")
            example_bp.bitproto
        """
        out_base_name = self.proto.name
        if self.proto.filepath:
            proto_base_name = os.path.basename(self.proto.filepath)
            out_base_name = os.path.splitext(proto_base_name)[0]  # remove extension
        out_filename = out_base_name + "_bp" + extension
        out_filepath = os.path.join(self.outdir, out_filename)
        return out_filepath

    # Belows should be implemented.

    def render(self) -> None:
        """Render current proto to file(s).
        This should be overided by subclasses.
        """
        raise NotImplementedError

    def render_proto_docstring(self) -> List[str]:
        """Returns the docstring of the proto file."""
        raise NotImplementedError


def render(proto: Proto, lang: str, outdir: Optional[str] = None) -> None:
    """Render given `proto` to directory `outdir`."""
    renderer_cls = get_renderer_cls(lang)
    if renderer_cls is None:
        raise UnsupportedLanguageToRender()

    renderer = renderer_cls(proto, outdir=outdir)
    renderer.render()
