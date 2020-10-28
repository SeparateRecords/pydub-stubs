from __future__ import annotations

from typing import Callable, Literal, Tuple, Union

from .audio_segment import AudioSegment

def apply_mono_filter_to_each_channel(
    seg: AudioSegment,
    filter_fn: Callable[[AudioSegment], AudioSegment],
) -> AudioSegment: ...
def normalize(seg: AudioSegment, headroom: float = ...) -> AudioSegment: ...
def speedup(
    seg: AudioSegment,
    playback_speed: float = ...,
    chunk_size: int = ...,
    crossfade: int = ...,
) -> AudioSegment: ...
def strip_silence(
    seg: AudioSegment,
    silence_len: int = ...,
    silence_thresh: int = ...,
    padding: int = ...,
) -> AudioSegment: ...
def compress_dynamic_range(
    seg: AudioSegment,
    threshold: float = ...,
    ratio: float = ...,
    attack: float = ...,
    release: float = ...,
) -> AudioSegment: ...
def invert_phase(
    seg: AudioSegment,
    channels: Union[
        Tuple[Literal[1], Literal[1]],
        Tuple[Literal[1], Literal[0]],
        Tuple[Literal[0], Literal[1]],
    ] = ...,
) -> AudioSegment: ...
def low_pass_filter(seg: AudioSegment, cutoff: float) -> AudioSegment: ...
def high_pass_filter(seg: AudioSegment, cutoff: float) -> AudioSegment: ...
def pan(seg: AudioSegment, pan_amount: float) -> AudioSegment: ...
def apply_gain_stereo(
    seg: AudioSegment,
    left_gain: float = ...,
    right_gain: float = ...,
) -> AudioSegment: ...
