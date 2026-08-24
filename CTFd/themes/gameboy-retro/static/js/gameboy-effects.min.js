/**
 * CCA ARENA 8-Bit Retro Sound FX & Super Mario Chiptune BGM Engine
 * Web Audio API Synthesizer + Embedded HTML5 Base64 Audio
 */

(function () {
  const BLIP_WAV = "data:audio/wav;base64,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ayih16zXuNfE19DX29fn1/LX/tcK2Osn3yfUJ8gnvCexJ6UnmieOJ4MnidiU2J/Yq9i22MLYzdjY2OTYEScGJ/om7ybkJtgmzSbCJrcmqyZg2WvZdtmB2Y3ZmNmj2a7Zudk8JjEmJiYbJg8mBCb5Je4l4yXYJTPaPtpJ2lPaXtpp2nTaf9qK2mslYCVVJUslQCU1JSolHyUVJQolAdsM2xbbIdss2zbbQdtM21bbnySUJIokfyR1JGokXyRVJEokwNvL29Xb4Nvq2/Xb/9sK3BTcHtzXI80jwiO4I64joyOZI48jhCOG3JDcm9yl3K/cudzE3M7c2NweIxQjCSP/IvUi6yLhItcizSI93UjdUt1c3WbdcN163YTdjt1oIl4iVCJKIkAiNiIsIiMiGSLx3fvdBd4P3hneIt4s3jbeQN62IawhoyGZIY8hhSF8IXIhaCGh3qvetd6+3sje0t7b3uXe7t4IIf4g9SDrIOIg2CDPIMUgvCBO31ffYd9q33Tffd+H35Dfmt9dIFQgSiBBIDggLiAlIBwgEiD33wDgCuAT4BzgJeAv4Djgvx+2H60fox+aH5EfiB9/H3YflOCd4Kbgr+C44MHgyuDT4NzgGx8SHwkfAB/3Hu4e5R7cHi3hNuE/4UjhUeFa4WPhbOF04YMeeh5xHmgeXx5XHk4eRR48Hs3h1eHe4efh8OH44QHiCuLuHeUd3B3UHcsdwh26HbEdqB1g4mniceJ64oPii+KU4pziWx1THUodQh05HTEdKB0gHRcd8eL54gLjCuMT4xvjI+Ms48wcxBy7HLMcqhyiHJockhyJHH/jh+OQ45jjoOOo47DjueM/HDccLxwnHB4cFhwOHAYcAuQK5BLkG+Qj5CvkM+Q75L0btRutG6UbnRuVG40bhRt9G4vkk+Sb5KPkq+Sz5Lvkw+Q2Gy4bJhseGxYbDhsGG/4aCeUR5RnlIeUp5TDlOOVA5bgasRqpGqEamRqSGooaghp7Go3lleWc5aTlrOWz5bvlw+U2Gi4aJxofGhcaEBoIGgEaB+YO5hbmHeYl5izmNOY75r0ZthmuGacZnxmYGZAZiRl+5obmjeaV5pzmo+ar5rLmRxk/GTgZMRkpGSIZGxkTGfTm++YC5wrnEecY5x/nJufSGMsYxBi9GLYYrhinGKAYZ+du53XnfOeE54vnkueZ52AYWRhSGEsYRBg9GDYY0efY59/n5uft5/Tn++cC6PcX8BfpF+IX2xfUF80XxhdB6EfoTuhV6FzoY+hq6HHoiReCF3sXdBdtF2YXYBdZF67otei76MLoyejQ6NboIxccFxYXDxcIFwEX+xb0FhPpGekg6SbpLek06TrpQem4FrIWqxalFp4WmBaRFnbpfOmD6YnpkOmW6Z3po+lWFlAWSRZDFjwWNhYwFikW3enk6erp8en36f3pBOr2FfAV6RXjFdwV1hXQFckVPepD6knqUOpW6lzqY+qXFZEVixWEFX4VeBVyFWsVm+qh6qfqreq06rrqwOo6FTQVLhUnFSEVGxUVFQ8V9+r96gPrCesQ6xbrHOveFNgU0hTMFMYUwBS6FLQUUutY617rZOtq63DrduuEFH4UeBRyFGwUZhRhFKXrq+ux67frvevD68nrz+ssFCYUIBQaFBQUDhQJFP3rA+wJ7A/sFOwa7CDs2hPVE88TyRPDE74TuBOyE1TsWexf7GXsauxw7HbshRN/E3kTdBNuE2gTYxOj7Knsruy07Lnsv+zF7DYTMBMrEyUTIBMaExUTDxP37PzsAu0H7Q3tEu0Y7eMS3RLYEtMSzRLIEsISQ+1J7U7tVO1Z7V7tZO2XEpESjBKHEoESfBJ3Eo/tlO2a7Z/tpO2q7a/tTBJHEkESPBI3EjESLBLZ7d7t5O3p7e7t8+357QIS/RH4EfIR7RHoEeMR3hEo7i3uMu437jzuQe5H7rQRrxGqEaURoBGbEZYRcO517nruf+6E7onuju5tEWgRYxFeEVkRVBFPEbbuu+7A7sXuyu7P7iwRJxEiER0RGBETEQ4R9+787gHvBu8L7xDvFe/mEOIQ3RDYENMQzhDJEDzvQe9G70rvT+9U71nvohCdEJkQlBCPEIoQhRB/74Tvie+O75Lvl++c718QWhBWEFEQTBBIEEMQwu/H78vv0O/V79nvIhAdEBkQFBAPEAsQBhD/7wPwCPAN8BHwFvAb8OEP3A/YD9MPzg/KD8UPP/BE8EjwTfBS8FbwW/ChD5wPmA+TD48Pig968H/wg/CI8IzwkfCV8GYPYg9dD1kPVA9QD0wPufC98MLwxvDL8M/wLQ8oDyQPHw8bDxcPEg/y8Pbw+/D/8ATxCPEM8e8O6w7nDuIO3g7aDivxL/Ez8TfxPPFA8UTxtw6zDq8Oqw6mDqIOng5m8Wvxb/Fz8Xfxe/GADnwOeA50DnAOaw5nDp3xofGl8arxrvGy8UoORg5CDj4OOQ41DjEO0/HX8dvx3/Hj8efxFA4QDgwOCA4EDgAO/A0I8gzyEPIU8hjyHPLgDdwN2A3UDdANzA3IDTzyQPJE8kjyTPJQ8qwNqA2kDaANnA2YDZQNcPJ08njyfPKA8oTyeQ11DXENbQ1pDWUNn/Kj8qfyqvKu8rLytvJGDUINPg07DTcNMw3R8tXy2fLc8uDy5PLo8hQNEQ0NDQkNBQ0BDQLzBvMK8w7zEfMV8+cM4wzgDNwM2AzUDNEMM/M38zrzPvNC80bztwyzDK8MrAyoDKQMX/Nj82fzavNu83LzdfOHDIQMgAx8DHkMdQyP85LzlvOZ853zofNcDFgMVQxRDE0MSgy6873zwfPE88jzy/PP8y4MKgwmDCMMHwwcDOjz6/Pv8/Lz9vP58wMMAAz8C/kL9QvyCxH0FfQY9Bz0H/Qj9NoL1gvTC9ALzAvJC8ULPvRC9EX0SPRM9E/0rQuqC6cLowugC50LZ/Rq9G70cfR09A==";

  let audioCtx = null;
  let soundEnabled = localStorage.getItem('gb_sound_enabled') !== 'false';
  let bgmPlaying = false;
  let bgmTimeout = null;

  function getAudioContext() {
    if (!audioCtx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) audioCtx = new AudioCtx();
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume().catch(() => {});
    }
    return audioCtx;
  }

  function playBlip() {
    if (!soundEnabled) return;
    try {
      const snd = new Audio(BLIP_WAV);
      snd.volume = 0.6;
      snd.play().catch(() => {});
    } catch (e) {}
  }

  /* --------------------------------------------------------------------------
     SUPER MARIO BROS. CHIPTUNE MELODY SEQUENCE
     -------------------------------------------------------------------------- */
  const N = {
    REST: 0,
    C4: 261.63, D4: 293.66, E4: 329.63, F4: 349.23, G4: 392.00, A4: 440.00, Bb4: 466.16, B4: 493.88,
    C5: 523.25, D5: 587.33, Ds5: 622.25, E5: 659.25, F5: 698.46, Fs5: 739.99, G5: 783.99, A5: 880.00, B5: 987.77,
    C6: 1046.50
  };

  const MARIO_MELODY = [
    // Intro
    [N.E5, 1.5], [N.E5, 1.5], [N.REST, 1.5], [N.E5, 1.5], [N.REST, 1.5], [N.C5, 1.5], [N.E5, 2.5], [N.G5, 3.5], [N.REST, 3.5], [N.G4, 3.5], [N.REST, 3.5],

    // Part A
    [N.C5, 2.5], [N.REST, 1.5], [N.G4, 2.5], [N.REST, 1.5], [N.E4, 2.5], [N.REST, 1.5],
    [N.A4, 2.0], [N.B4, 2.0], [N.Bb4, 1.5], [N.A4, 2.5],
    [N.G4, 1.5], [N.E5, 1.5], [N.G5, 1.5], [N.A5, 2.5], [N.F5, 1.5], [N.G5, 1.5],
    [N.E5, 2.5], [N.C5, 1.5], [N.D5, 1.5], [N.B4, 3.0],

    // Repeat Hook
    [N.C5, 2.5], [N.REST, 1.5], [N.G4, 2.5], [N.REST, 1.5], [N.E4, 2.5], [N.REST, 1.5],
    [N.A4, 2.0], [N.B4, 2.0], [N.Bb4, 1.5], [N.A4, 2.5],
    [N.G4, 1.5], [N.E5, 1.5], [N.G5, 1.5], [N.A5, 2.5], [N.F5, 1.5], [N.G5, 1.5],
    [N.E5, 2.5], [N.C5, 1.5], [N.D5, 1.5], [N.B4, 3.0]
  ];

  function playMarioNote(ctx, freq, startTime, duration) {
    if (freq <= 0) return;
    try {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = 'square';
      osc.frequency.setValueAtTime(freq, startTime);

      gain.gain.setValueAtTime(0.12, startTime);
      gain.gain.exponentialRampToValueAtTime(0.001, startTime + duration * 0.95);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start(startTime);
      osc.stop(startTime + duration);
    } catch (e) {}
  }

  function scheduleMarioLoop() {
    if (!bgmPlaying) return;
    const ctx = getAudioContext();
    if (!ctx) return;
    if (ctx.state === 'suspended') ctx.resume();

    const tempo = 0.09; // Tempo duration multiplier
    let curTime = ctx.currentTime + 0.05;

    MARIO_MELODY.forEach(([freq, beats]) => {
      const dur = beats * tempo;
      if (freq > 0) {
        playMarioNote(ctx, freq, curTime, dur);
      }
      curTime += dur;
    });

    const loopMs = (curTime - ctx.currentTime) * 1000;
    bgmTimeout = setTimeout(() => {
      if (bgmPlaying) scheduleMarioLoop();
    }, Math.max(100, loopMs - 60));
  }

  function startBGM() {
    bgmPlaying = true;
    const ctx = getAudioContext();
    if (ctx && ctx.state === 'suspended') {
      ctx.resume().then(() => scheduleMarioLoop()).catch(() => scheduleMarioLoop());
    } else {
      scheduleMarioLoop();
    }
  }

  function stopBGM() {
    bgmPlaying = false;
    if (bgmTimeout) {
      clearTimeout(bgmTimeout);
      bgmTimeout = null;
    }
  }

  function updateButtonsUI() {
    const sfxBtn = document.querySelector('.sound-toggle-btn');
    if (sfxBtn) {
      const text = sfxBtn.querySelector('#sfx-status-text');
      if (text) text.innerText = soundEnabled ? 'SFX: ON' : 'SFX: OFF';
      sfxBtn.style.backgroundColor = soundEnabled ? 'var(--pop-teal)' : '#64748b';
    }

    const bgmBtn = document.querySelector('.bgm-toggle-btn');
    if (bgmBtn) {
      const text = bgmBtn.querySelector('#bgm-status-text');
      if (text) text.innerText = bgmPlaying ? 'BGM: ON' : 'BGM: OFF';
      bgmBtn.style.backgroundColor = bgmPlaying ? 'var(--pop-pink)' : '#64748b';
    }
  }

  function toggleSound() {
    soundEnabled = !soundEnabled;
    localStorage.setItem('gb_sound_enabled', soundEnabled ? 'true' : 'false');
    updateButtonsUI();
    if (soundEnabled) playBlip();
    return soundEnabled;
  }

  function toggleBGM() {
    if (bgmPlaying) {
      stopBGM();
    } else {
      startBGM();
    }
    updateButtonsUI();
    return bgmPlaying;
  }

  // Expose global methods
  window.GameBoyAudio = {
    playBlip: playBlip,
    toggleSound: toggleSound,
    toggleBGM: toggleBGM,
    isSoundEnabled: function () { return soundEnabled; },
    isBGMPlaying: function () { return bgmPlaying; }
  };

  window.toggleSFX = toggleSound;
  window.toggleBGM = toggleBGM;

  // Initialize UI & Event Listeners
  function initAudioListeners() {
    updateButtonsUI();

    const sfxBtn = document.querySelector('.sound-toggle-btn');
    if (sfxBtn && !sfxBtn._bound) {
      sfxBtn._bound = true;
      sfxBtn.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        toggleSound();
      });
    }

    const bgmBtn = document.querySelector('.bgm-toggle-btn');
    if (bgmBtn && !bgmBtn._bound) {
      bgmBtn._bound = true;
      bgmBtn.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        toggleBGM();
      });
    }

    document.addEventListener('click', function (e) {
      const target = e.target.closest('button, .btn, .nav-link, .challenge-card-btn, .navbar-brand');
      if (target && !target.classList.contains('sound-toggle-btn') && !target.classList.contains('bgm-toggle-btn')) {
        playBlip();
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAudioListeners);
  } else {
    initAudioListeners();
  }
})();
