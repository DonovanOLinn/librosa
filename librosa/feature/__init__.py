#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Feature extraction
==================

Spectral features
-----------------

.. autosummary::
    :toctree: generated/

    chroma_stft
    chroma_cqt
    chroma_cens
    melspectrogram
    mfcc
    rms
    spectral_centroid
    spectral_bandwidth
    spectral_contrast
    spectral_flatness
    spectral_rolloff
    poly_features
    tonnetz
    zero_crossing_rate

Rhythm features
---------------
.. autosummary::
    :toctree: generated/

    tempogram
    fourier_tempogram

Feature manipulation
--------------------

.. autosummary::
    :toctree: generated/

    delta
    stack_memory


Feature inversion
-----------------

.. autosummary::
    :toctree: generated

    inverse.mel_to_stft
    inverse.mel_to_audio
    inverse.mfcc_to_mel
    inverse.mfcc_to_audio
"""

import lazy_loader as lazy

__getattr__, __dir__, __all__ = lazy.attach_stub(__name__, __file__)
