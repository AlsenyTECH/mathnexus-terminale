# -*- coding: utf-8 -*-
"""Voix « Pierre » (Piper fr_FR-upmc-medium, locuteur 1, CC BY-SA 4.0).

    from voix import dire
    duree = dire("Le texte.", "sortie.wav")

Modèle : archive sherpa-onnx « vits-piper-fr_FR-upmc-medium » (release tts-models),
dossier indiqué par VOIX_DIR (défaut ~/voices/vits-piper-fr_FR-upmc-medium).
Pour une autre voix au même format (par exemple celle de MathNexus après entraînement),
il suffit de changer VOIX_ONNX et LOCUTEUR.
"""
import os, wave
from piper import PiperVoice, SynthesisConfig

VOIX_DIR = os.environ.get("VOIX_DIR", os.path.expanduser("~/voices/vits-piper-fr_FR-upmc-medium"))
VOIX_ONNX = os.environ.get("VOIX_ONNX", os.path.join(VOIX_DIR, "fr_FR-upmc-medium.onnx"))
LOCUTEUR = int(os.environ.get("VOIX_LOCUTEUR", "1"))
_V = None

def dire(texte, sortie, vitesse=1.04):
    global _V
    if _V is None:
        _V = PiperVoice.load(VOIX_ONNX)
    cfg = SynthesisConfig(speaker_id=LOCUTEUR, length_scale=vitesse)
    with wave.open(sortie, "wb") as w:
        _V.synthesize_wav(texte, w, syn_config=cfg)
    with wave.open(sortie) as w:
        return w.getnframes() / w.getframerate()
