/**
 * CCA ARENA 8-Bit Retro Sound FX & Super Mario Chiptune BGM Engine
 * Web Audio API Synthesizer + Embedded HTML5 Base64 Audio
 */

(function () {
  const BLIP_WAV = "data:audio/wav;base64,UklGRqQPAABXQVZFZm10IBAAAAABAAEAIlYAAESsAAACABAAZGF0YYAPAACgkkBtIG0AbeFswWyibIJsY2xDbCRsBGzla8Zrp2uHa2hrSWsqa/WUFJUzlVKVcZWQla+VzpXtlQuWKpZJlmiWhpallsOW4pYAl+Fow2ikaIZoaGhJaCtoDWjvZ9FnsmeUZ3ZnWGc6Zxxn/2YfmT2ZW5l5mZeZtJnSmfCZDZormkiaZpqDmqGavprbmvma6mTNZK9kkmR1ZFhkO2QeZAFk5GPHY6pjjWNwY1NjNmMZYwOdIJ09nVmddp2Tna+dzJ3onQWeIZ49nlqedp6Snq+ey54ZYf1g4WDFYKhgjGBwYFRgOGAdYAFg5V/JX61fkV92X1pfwqDdoPmgFKEwoUuhZ6GCoZ6huaHUofChC6ImokKiXaKIXW1dUl03XRxdAV3mXMtcsFyVXHpcX1xFXCpcD1z0WyakQaRcpHakkaSrpMak4KT7pBWlL6VKpWSlfqWZpbOlM1oZWv9Z5VnKWbBZlll8WWJZSFkvWRVZ+1jhWMdYUqdsp4anoKe5p9On7KcGqB+oOahSqGyohaifqLio0agVV/xW41bKVrFWl1Z+VmVWTFYzVhpWAVboVc9VtlVjqnuqlKqtqsaq3qr3qhCrKKtBq1qrcquLq6OrvKssVBNU+1PjU8pTslOaU4JTaVNRUzlTIVMJU/FS2VJArVitb62HrZ+tt63Preet/60Xri6uRq5ernWuc1FbUURRLFEVUf1Q5lDOULdQn1CIUHBQWVBCUCtQ7a8EsBuwMrBJsGGweLCPsKawvbDUsOuwArEZsdBOuk6jToxOdU5eTkhOMU4aTgRO7U3WTcBNqU1tsoSymrKxssey3rL0sgqzIbM3s02zY7N6s5CzWkxETC5MGEwCTOtL1Uu/S6lLlEt+S2hLUks8S9q08LQFtRu1MbVHtVy1crWItZ21s7XItd6187X3SeJJzEm3SaFJjEl3SWFJTEk3SSJJDEn3SOJIM7dIt123creHt5y3sbfGt9u38LcFuBq4L7i8R6dHk0d+R2lHVEdARytHFkcCR+1G2UbERlC5Zbl5uY65orm3ucu537n0uQi6HLoxukW6p0WTRX5FakVWRUJFLkUaRQZF8kTeRMpEtkSiRHK7hruau667wbvVu+m7/bsQvCS8OLxLvKFDjUN6Q2ZDU0M/QytDGEMFQ/FC3kLKQrdCXL1wvYO9lr2qvb290L3jvfa9Cr4dvjC+Q76qQZdBhEFxQV5BS0E4QSVBEkH/QOxA2kDHQEy/X79yv4S/l7+qv7y/z7/iv/S/B8AZwNQ/wj+vP50/ij94P2U/Uz9BPy4/HD8KPwnBG8EtwT/BUsFkwXbBiMGawazBvsHQwePBCz75Peg91j3EPbI9oD2OPXw9aj1YPUc9y8Ldwu/CAMMSwyTDNcNHw1nDasN8w43DYTxQPD48LTwbPAo8+DvnO9Y7xDuzO6I7cMSBxJLEpMS1xMbE18ToxPnEC8UcxS3FwjqxOqA6jzp+Om06XDpLOjo6KToZOgg6CcYaxivGPMZMxl3GbsZ+xo/GoMawxj85LjkeOQ05/TjsONw4yzi7OKo4mjiJOIfHl8eox7jHycfZx+nH+ccKyBrIKsjGN7Y3pTeVN4U3dTdlN1U3RTc1NyU3FTf7yAvJG8kryTvJS8lbyWvJesmKyZrJVjZGNjc2JzYXNgg2+DXoNdk1yTW5Nao1Zsp1yoXKlMqkyrPKw8rSyuLK8coAy/A04TTRNMI0szSkNJQ0hTR2NGc0VzS4y8fL1svly/TLBMwTzCLMMcxAzE/MojOTM4QzdTNmM1gzSTM6MyszHDMNMwLNEM0fzS7NPc1LzVrNac13zYbNlc1dMk4yPzIxMiIyFDIFMvcx6DHaMcsxQ85SzmDObs59zovOms6ozrbOxM7Tzh8xETEDMfQw5jDYMMowvDCtMJ8wb899z4vPmc+nz7XPw8/Rz9/P7c/7z/cv6S/bL80vwC+yL6Qvli+IL3ovk9Ch0K/QvdDK0NjQ5tDz0AHRD9Ec0dYuyS67Lq0uoC6SLoUudy5qLlwusdG+0czR2dHn0fTRAdIP0hzSKdI30rwtry2iLZQthy16LW0tYC1SLUUtyNLV0uLS79L80gnTFtMj0zDTPdO2LKksnCyPLIIsdSxoLFssTixBLDUs2NPl0/LT/9ML1BjUJdQy1D7US9SoK5wrjyuCK3YraStcK1ArQys3K9bU4tTv1PvUCNUU1SHVLdU61UbVriqhKpUqiSp8KnAqZCpXKksqPyrO1drV5tXy1f7VC9YX1iPWL9Y71rkprSmhKZQpiCl8KXApZClYKUwpwNbM1tjW5Nbv1vvWB9cT1x/X1SjJKL0osiimKJoojiiCKHcoayih16zXuNfE19DX29fn1/LX/tcK2Osn3yfUJ8gnvCexJ6UnmieOJ4MnidiU2J/Yq9i22MLYzdjY2OTYEScGJ/om7ybkJtgmzSbCJrcmqyZg2WvZdtmB2Y3ZmNmj2a7Zudk8JjEmJiYbJg8mBCb5Je4l4yXYJTPaPtpJ2lPaXtpp2nTaf9qK2mslYCVVJUslQCU1JSolHyUVJQolAdsM2xbbIdss2zbbQdtM21bbnySUJIokfyR1JGokXyRVJEokwNvL29Xb4Nvq2/Xb/9sK3BTcHtzXI80jwiO4I64joyOZI48jhCOG3JDcm9yl3K/cudzE3M7c2NweIxQjCSP/IvUi6yLhItcizSI93UjdUt1c3WbdcN163YTdjt1oIl4iVCJKIkAiNiIsIiMiGSLx3fvdBd4P3hneIt4s3jbeQN62IawhoyGZIY8hhSF8IXIhaCGh3qvetd6+3sje0t7b3uXe7t4IIf4g9SDrIOIg2CDPIMUgvCBO31ffYd9q33Tffd+H35Dfmt9dIFQgSiBBIDggLiAlIBwgEiD33wDgCuAT4BzgJeAv4Djgvx+2H60fox+aH5EfiB9/H3YflOCd4Kbgr+C44MHgyuDT4NzgGx8SHwkfAB/3Hu4e5R7cHi3hNuE/4UjhUeFa4WPhbOF04YMeeh5xHmgeXx5XHk4eRR48Hs3h1eHe4efh8OH44QHiCuLuHeUd3B3UHcsdwh26HbEdqB1g4mniceJ64oPii+KU4pziWx1THUodQh05HTEdKB0gHRcd8eL54gLjCuMT4xvjI+Ms48wcxBy7HLMcqhyiHJockhyJHH/jh+OQ45jjoOOo47DjueM/HDccLxwnHB4cFhwOHAYcAuQK5BLkG+Qj5CvkM+Q75L0btRutG6UbnRuVG40bhRt9G4vkk+Sb5KPkq+Sz5Lvkw+Q2Gy4bJhseGxYbDhsGG/4aCeUR5RnlIeUp5TDlOOVA5bgasRqpGqEamRqSGooaghp7Go3lleWc5aTlrOWz5bvlw+U2Gi4aJxofGhcaEBoIGgEaB+YO5hbmHeYl5izmNOY75r0ZthmuGacZnxmYGZAZiRl+5obmjeaV5pzmo+ar5rLmRxk/GTgZMRkpGSIZGxkTGfTm++YC5wrnEecY5x/nJufSGMsYxBi9GLYYrhinGKAYZ+du53XnfOeE54vnkueZ52AYWRhSGEsYRBg9GDYY0efY59/n5uft5/Tn++cC6PcX8BfpF+IX2xfUF80XxhdB6EfoTuhV6FzoY+hq6HHoiReCF3sXdBdtF2YXYBdZF67otei76MLoyejQ6NboIxccFxYXDxcIFwEX+xb0FhPpGekg6SbpLek06TrpQem4FrIWqxalFp4WmBaRFnbpfOmD6YnpkOmW6Z3po+lWFlAWSRZDFjwWNhYwFikW3enk6erp8en36f3pBOr2FfAV6RXjFdwV1hXQFckVPepD6knqUOpW6lzqY+qXFZEVixWEFX4VeBVyFWsVm+qh6qfqreq06rrqwOo6FTQVLhUnFSEVGxUVFQ8V9+r96gPrCesQ6xbrHOveFNgU0hTMFMYUwBS6FLQUUutY617rZOtq63DrduuEFH4UeBRyFGwUZhRhFKXrq+ux67frvevD68nrz+ssFCYUIBQaFBQUDhQJFP3rA+wJ7A/sFOwa7CDs2hPVE88TyRPDE74TuBOyE1TsWexf7GXsauxw7HbshRN/E3kTdBNuE2gTYxOj7Knsruy07Lnsv+zF7DYTMBMrEyUTIBMaExUTDxP37PzsAu0H7Q3tEu0Y7eMS3RLYEtMSzRLIEsISQ+1J7U7tVO1Z7V7tZO2XEpESjBKHEoESfBJ3Eo/tlO2a7Z/tpO2q7a/tTBJHEkESPBI3EjESLBLZ7d7t5O3p7e7t8+357QIS/RH4EfIR7RHoEeMR3hEo7i3uMu437jzuQe5H7rQRrxGqEaURoBGbEZYRcO517nruf+6E7onuju5tEWgRYxFeEVkRVBFPEbbuu+7A7sXuyu7P7iwRJxEiER0RGBETEQ4R9+787gHvBu8L7xDvFe/mEOIQ3RDYENMQzhDJEDzvQe9G70rvT+9U71nvohCdEJkQlBCPEIoQhRB/74Tvie+O75Lvl++c718QWhBWEFEQTBBIEEMQwu/H78vv0O/V79nvIhAdEBkQFBAPEAsQBhD/7wPwCPAN8BHwFvAb8OEP3A/YD9MPzg/KD8UPP/BE8EjwTfBS8FbwW/ChD5wPmA+TD48Pig968H/wg/CI8IzwkfCV8GYPYg9dD1kPVA9QD0wPufC98MLwxvDL8M/wLQ8oDyQPHw8bDxcPEg/y8Pbw+/D/8ATxCPEM8e8O6w7nDuIO3g7aDivxL/Ez8TfxPPFA8UTxtw6zDq8Oqw6mDqIOng5m8Wvxb/Fz8Xfxe/GADnwOeA50DnAOaw5nDp3xofGl8arxrvGy8UoORg5CDj4OOQ41DjEO0/HX8dvx3/Hj8efxFA4QDgwOCA4EDgAO/A0I8gzyEPIU8hjyHPLgDdwN2A3UDdANzA3IDTzyQPJE8kjyTPJQ8qwNqA2kDaANnA2YDZQNcPJ08njyfPKA8oTyeQ11DXENbQ1pDWUNn/Kj8qfyqvKu8rLytvJGDUINPg07DTcNMw3R8tXy2fLc8uDy5PLo8hQNEQ0NDQkNBQ0BDQLzBvMK8w7zEfMV8+cM4wzgDNwM2AzUDNEMM/M38zrzPvNC80bztwyzDK8MrAyoDKQMX/Nj82fzavNu83LzdfOHDIQMgAx8DHkMdQyP85LzlvOZ853zofNcDFgMVQxRDE0MSgy6873zwfPE88jzy/PP8y4MKgwmDCMMHwwcDOjz6/Pv8/Lz9vP58wMMAAz8C/kL9QvyCxH0FfQY9Bz0H/Qj9NoL1gvTC9ALzAvJC8ULPvRC9EX0SPRM9E/0rQuqC6cLowugC50LZ/Rq9G70cfR09A==";

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

  /* --------------------------------------------------------------------------
     FIRST BLOOD VICTORY FANFARE (RETRO SYNTH CHIPTUNE)
     -------------------------------------------------------------------------- */
  function playFirstBloodFanfare() {
    try {
      const ctx = getAudioContext();
      if (!ctx) return;
      if (ctx.state === 'suspended') {
        ctx.resume().catch(() => {});
      }

      const now = ctx.currentTime + 0.05;
      
      // Triumphant Victory Chime: C5, E5, G5, C6 (pause) -> G5, C6 + E6 chord
      const notes = [
        { f: 523.25, t: 0.00, d: 0.12, type: 'triangle' }, // C5
        { f: 659.25, t: 0.12, d: 0.12, type: 'triangle' }, // E5
        { f: 783.99, t: 0.24, d: 0.12, type: 'triangle' }, // G5
        { f: 1046.50, t: 0.36, d: 0.30, type: 'triangle' }, // C6
        { f: 783.99, t: 0.70, d: 0.12, type: 'triangle' }, // G5
        { f: 1046.50, t: 0.82, d: 0.65, type: 'triangle' }, // C6 (triumph finale)
        { f: 1318.51, t: 0.82, d: 0.65, type: 'sine' }      // E6 (harmonizer)
      ];

      notes.forEach(n => {
        try {
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = n.type || 'triangle';
          osc.frequency.setValueAtTime(n.f, now + n.t);
          
          gain.gain.setValueAtTime(0.25, now + n.t);
          gain.gain.exponentialRampToValueAtTime(0.001, now + n.t + n.d);

          osc.connect(gain);
          gain.connect(ctx.destination);

          osc.start(now + n.t);
          osc.stop(now + n.t + n.d);
        } catch (e) {}
      });
    } catch (e) {}
  }

  /* --------------------------------------------------------------------------
     FIRST BLOOD CELEBRATION TOAST & SPARKLE BANNER
     -------------------------------------------------------------------------- */
  let lastBannerShownTime = 0;
  let lastBannerChallenge = '';

  function showFirstBloodBanner(data) {
    if (!data) data = {};

    let solver = data.solver;
    let challenge = data.challenge;
    if (!solver && data.content && data.content.includes(' baru saja')) {
      solver = data.content.split(' baru saja')[0].trim();
    }
    if (!challenge && data.title && data.title.includes('//')) {
      challenge = data.title.split('//')[1].trim();
    }
    if (!solver) solver = data.title ? data.title.split('//')[0].trim() : 'Seseorang';
    if (!challenge) challenge = data.title || 'Tantangan';

    const cleanChal = challenge.toLowerCase().trim();
    const now = Date.now();
    
    // Strict Global Debounce: Never trigger the same challenge within 30 seconds, or ANY banner within 4 seconds
    if ((now - lastBannerShownTime < 30000 && lastBannerChallenge === cleanChal) || (now - lastBannerShownTime < 4000)) {
      return;
    }
    lastBannerShownTime = now;
    lastBannerChallenge = cleanChal;

    // Play fanfare once
    playFirstBloodFanfare();

    let container = document.getElementById('first-blood-container');
    if (!container) {
      container = document.createElement('div');
      container.id = 'first-blood-container';
      if (document.body) {
        document.body.appendChild(container);
      } else {
        document.documentElement.appendChild(container);
      }
    }

    // Always clear container so multiple banners can NEVER stack!
    container.innerHTML = '';

    const category = data.category || 'CTF';
    const points = data.value ? `+${data.value} PTS` : '';

    const bannerId = 'fb-' + now;
    const bannerHtml = `
      <div class="first-blood-banner" id="${bannerId}">
        <div class="fb-badge-tag">
          <i class="fas fa-crown text-warning me-1"></i> FIRST BLOOD // PENAKLUK PERDANA
        </div>
        <div class="fb-title-text">
          <span class="fb-solver-name me-2"><i class="fas fa-user-ninja me-1 text-danger"></i>${solver}</span>
          <span class="fb-action-text me-2">baru saja merebut</span>
          <span class="fb-chal-name me-2">${challenge}</span>
          ${points ? `<span class="badge bg-warning text-dark fb-pts-badge">${points}</span>` : ''}
        </div>
        <div class="fb-category-tag"><i class="fas fa-layer-group me-1"></i> Kategori: <strong>${category.toUpperCase()}</strong></div>
        <button type="button" class="fb-close-btn" onclick="document.getElementById('${bannerId}').remove()">&times;</button>
      </div>
    `;

    container.innerHTML = bannerHtml;

    // Auto remove after 6.5 seconds
    setTimeout(() => {
      const banner = document.getElementById(bannerId);
      if (banner) {
        banner.classList.add('fb-fade-out');
        setTimeout(() => banner.remove(), 350);
      }
    }, 6500);
  }

  window.showFirstBloodBanner = showFirstBloodBanner;
  window.triggerTestFirstBlood = function(solver, chal, cat, pts) {
    showFirstBloodBanner({
      solver: solver || 'AcehCyberNinja',
      challenge: chal || 'Small Exponent RSA Attack',
      category: cat || 'Crypto',
      value: pts || 300
    });
  };

  // Expose global methods
  window.GameBoyAudio = {
    playBlip: playBlip,
    playFirstBloodFanfare: playFirstBloodFanfare,
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

  /* --------------------------------------------------------------------------
     CUSTOM HIGH-TECH CYBER MODAL CONFIRM & ALERT DIALOGS
     -------------------------------------------------------------------------- */
  function createCyberModalContainer() {
    let container = document.getElementById('cyber-modal-container');
    if (!container) {
      container = document.createElement('div');
      container.id = 'cyber-modal-container';
      document.body.appendChild(container);
    }
    return container;
  }

  function showCyberConfirm(options) {
    return new Promise((resolve) => {
      const container = createCyberModalContainer();
      const title = options.title || 'Konfirmasi Tindakan';
      const text = options.text || 'Apakah Anda yakin ingin melanjutkan?';
      const confirmText = options.confirmText || 'Ya, Lanjutkan';
      const cancelText = options.cancelText || 'Batal';
      const icon = options.icon || '<i class="fas fa-lightbulb text-warning"></i>';
      const highlight = options.highlight || '';

      const modalHtml = `
        <div class="cyber-modal-backdrop" id="cyber-confirm-modal">
          <div class="cyber-modal-card">
            <div class="cyber-modal-icon-badge">${icon}</div>
            <h3 class="cyber-modal-title">${title}</h3>
            <div class="cyber-modal-body">${text}</div>
            ${highlight ? `<div class="cyber-modal-highlight">${highlight}</div>` : ''}
            <div class="cyber-modal-actions">
              <button type="button" class="btn btn-outline-secondary cyber-btn-cancel" id="cyber-modal-cancel">
                <i class="fas fa-times me-1"></i> ${cancelText}
              </button>
              <button type="button" class="btn btn-primary cyber-btn-confirm" id="cyber-modal-confirm">
                <i class="fas fa-unlock me-1"></i> ${confirmText}
              </button>
            </div>
          </div>
        </div>
      `;

      container.innerHTML = modalHtml;
      playBlip();

      const modalEl = document.getElementById('cyber-confirm-modal');
      const confirmBtn = document.getElementById('cyber-modal-confirm');
      const cancelBtn = document.getElementById('cyber-modal-cancel');

      function cleanup(result) {
        if (modalEl) {
          modalEl.classList.add('cyber-modal-fadeout');
          setTimeout(() => {
            container.innerHTML = '';
            resolve(result);
          }, 180);
        } else {
          resolve(result);
        }
      }

      confirmBtn.addEventListener('click', () => cleanup(true));
      cancelBtn.addEventListener('click', () => cleanup(false));
      modalEl.addEventListener('click', (e) => {
        if (e.target === modalEl) cleanup(false);
      });

      const escHandler = (e) => {
        if (e.key === 'Escape') {
          document.removeEventListener('keydown', escHandler);
          cleanup(false);
        }
      };
      document.addEventListener('keydown', escHandler);
    });
  }

  function showCyberAlert(options) {
    return new Promise((resolve) => {
      const container = createCyberModalContainer();
      const title = options.title || 'Informasi';
      const text = options.text || '';
      const buttonText = options.buttonText || 'Tutup';
      const icon = options.icon || '<i class="fas fa-info-circle text-primary"></i>';

      const modalHtml = `
        <div class="cyber-modal-backdrop" id="cyber-alert-modal">
          <div class="cyber-modal-card">
            <div class="cyber-modal-icon-badge">${icon}</div>
            <h3 class="cyber-modal-title">${title}</h3>
            <div class="cyber-modal-body">${text}</div>
            <div class="cyber-modal-actions justify-content-center">
              <button type="button" class="btn btn-primary px-4 py-2" id="cyber-modal-ok">
                <i class="fas fa-check me-1"></i> ${buttonText}
              </button>
            </div>
          </div>
        </div>
      `;

      container.innerHTML = modalHtml;
      playBlip();

      const modalEl = document.getElementById('cyber-alert-modal');
      const okBtn = document.getElementById('cyber-modal-ok');

      function cleanup() {
        if (modalEl) {
          modalEl.classList.add('cyber-modal-fadeout');
          setTimeout(() => {
            container.innerHTML = '';
            resolve();
          }, 180);
        } else {
          resolve();
        }
      }

      okBtn.addEventListener('click', cleanup);
      modalEl.addEventListener('click', (e) => {
        if (e.target === modalEl) cleanup();
      });
    });
  }

  window.showCyberConfirm = showCyberConfirm;
  window.showCyberAlert = showCyberAlert;

  // Intercept CTFd functions
  function patchCTFdDialogs() {
    if (window.CTFd && window.CTFd._functions && window.CTFd._functions.challenge) {
      const fn = window.CTFd._functions.challenge;

      fn.displayHintUnlock = function(hint) {
        const cost = hint && hint.cost ? hint.cost : 0;
        const title = hint && hint.title ? `Petunjuk: ${hint.title}` : 'Buka Kunci Petunjuk';
        const highlightText = cost > 0 
          ? `<i class="fas fa-exclamation-circle text-warning me-1"></i> Poin Anda akan dikurangi sebesar <strong>${cost} PTS</strong>.` 
          : '<i class="fas fa-check-circle text-success me-1"></i> Petunjuk ini gratis (0 PTS).';

        return showCyberConfirm({
          title: title,
          text: 'Apakah Anda yakin ingin membuka petunjuk untuk tantangan ini?',
          highlight: highlightText,
          confirmText: cost > 0 ? `Buka (-${cost} PTS)` : 'Buka Petunjuk',
          cancelText: 'Batal',
          icon: '<i class="fas fa-lightbulb text-warning"></i>'
        });
      };

      fn.displayUnlock = function(target) {
        return showCyberConfirm({
          title: 'Buka Petunjuk',
          text: 'Apakah Anda yakin ingin membuka petunjuk ini?',
          highlight: '<i class="fas fa-exclamation-circle text-warning me-1"></i> Poin Anda akan dipotong untuk membuka petunjuk.',
          confirmText: 'Buka Sekarang',
          cancelText: 'Batal',
          icon: '<i class="fas fa-lightbulb text-warning"></i>'
        });
      };

      fn.displaySolutionUnlock = function(sol) {
        return showCyberConfirm({
          title: 'Buka Solusi / Writeup',
          text: 'Membuka kunci solusi akan menghentikan perolehan poin Anda untuk soal ini.',
          highlight: '<i class="fas fa-exclamation-triangle text-danger me-1"></i> Tindakan ini permanen dan tidak dapat dibatalkan.',
          confirmText: 'Ya, Buka Solusi',
          cancelText: 'Batal',
          icon: '<i class="fas fa-unlock text-primary"></i>'
        });
      };

      fn.displayUnlockError = function(err) {
        const errors = [];
        if (err && err.errors) {
          Object.keys(err.errors).forEach(k => errors.push(err.errors[k]));
        }
        const msg = errors.length > 0 ? errors.join('<br>') : 'Gagal membuka petunjuk. Pastikan poin Anda mencukupi!';
        return showCyberAlert({
          title: 'Gagal Membuka Kunci',
          text: msg,
          buttonText: 'Mengerti',
          icon: '<i class="fas fa-times-circle text-danger"></i>'
        });
      };

      fn.displayHint = function(hint) {
        const content = hint && hint.content ? hint.content : (hint && hint.html ? hint.html : '');
        return showCyberAlert({
          title: 'Petunjuk Tantangan',
          text: content,
          buttonText: 'Tutup',
          icon: '<i class="fas fa-lightbulb text-warning"></i>'
        });
      };
    }
  }

  /* --------------------------------------------------------------------------
     ALPINE CYBER HINT COMPONENT
     -------------------------------------------------------------------------- */
  window.CyberHint = function(id, cost, title) {
    return {
      id: id,
      cost: cost || 0,
      title: title || '',
      unlockedHtml: null,
      loading: false,
      async unlock() {
        if (this.loading) return;
        const confirmed = await window.showCyberConfirm({
          title: this.title ? `Petunjuk: ${this.title}` : 'Buka Kunci Petunjuk',
          text: 'Apakah Anda yakin ingin membuka petunjuk untuk tantangan ini?',
          highlight: this.cost > 0 
            ? `<i class="fas fa-exclamation-circle text-warning me-1"></i> Poin Anda akan dikurangi sebesar <strong>${this.cost} PTS</strong>.` 
            : '<i class="fas fa-check-circle text-success me-1"></i> Petunjuk ini gratis (0 PTS).',
          confirmText: this.cost > 0 ? `Buka (-${this.cost} PTS)` : 'Buka Sekarang',
          cancelText: 'Batal',
          icon: '<i class="fas fa-lightbulb text-warning"></i>'
        });

        if (!confirmed) return;

        this.loading = true;
        try {
          const checkRes = await fetch(`${window.init ? window.init.urlRoot : ''}/api/v1/hints/${this.id}`, {
            method: 'GET',
            headers: {
              'Accept': 'application/json',
              'CSRF-Token': window.init ? window.init.csrfNonce : ''
            }
          });
          const checkData = await checkRes.json();
          if (checkData.data && (checkData.data.content || checkData.data.html)) {
            this.unlockedHtml = checkData.data.html || checkData.data.content;
            this.loading = false;
            return;
          }

          const unlockRes = await fetch(`${window.init ? window.init.urlRoot : ''}/api/v1/unlocks`, {
            method: 'POST',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
              'CSRF-Token': window.init ? window.init.csrfNonce : ''
            },
            body: JSON.stringify({ target: this.id, type: 'hints' })
          });
          const unlockData = await unlockRes.json();

          if (unlockData.success) {
            const hintRes = await fetch(`${window.init ? window.init.urlRoot : ''}/api/v1/hints/${this.id}`, {
              method: 'GET',
              headers: {
                'Accept': 'application/json',
                'CSRF-Token': window.init ? window.init.csrfNonce : ''
              }
            });
            const hintData = await hintRes.json();
            if (hintData.data) {
              this.unlockedHtml = hintData.data.html || hintData.data.content;
            }
          } else {
            const errors = [];
            if (unlockData.errors) {
              Object.keys(unlockData.errors).forEach(k => errors.push(unlockData.errors[k]));
            }
            const msg = errors.length > 0 ? errors.join('<br>') : 'Gagal membuka petunjuk. Pastikan poin Anda mencukupi!';
            window.showCyberAlert({
              title: 'Gagal Membuka Petunjuk',
              text: msg,
              buttonText: 'Mengerti',
              icon: '<i class="fas fa-times-circle text-danger"></i>'
            });
          }
        } catch (e) {
          console.error(e);
        } finally {
          this.loading = false;
        }
      }
    };
  };

  /* --------------------------------------------------------------------------
     REAL-TIME DEDICATED SSE & AUTO-SYNC TELEMETRY ENGINE
     -------------------------------------------------------------------------- */
  let lastProcessedNotifId = parseInt(localStorage.getItem('cca_last_notif_id') || '0', 10);

  function initDedicatedSSE() {
    try {
      const urlRoot = window.init && window.init.urlRoot ? window.init.urlRoot : '';
      const sse = new EventSource(urlRoot + '/events');

      sse.addEventListener('notification', function(e) {
        try {
          const data = JSON.parse(e.data);
          if (data) {
            if (data.id && data.id > lastProcessedNotifId) {
              lastProcessedNotifId = data.id;
              localStorage.setItem('cca_last_notif_id', String(data.id));
            }
            if (data.type === 'first_blood' || (data.title && data.title.includes('FIRST BLOOD'))) {
              showFirstBloodBanner(data);
              // Trigger reactive UI updates
              window.dispatchEvent(new CustomEvent('load-challenges'));
              window.dispatchEvent(new CustomEvent('load-scoreboard'));
            }
          }
        } catch (err) {}
      });

      sse.onerror = function() {
        // Close cleanly on proxy error without console spam; auto-sync poller handles telemetry
        try { sse.close(); } catch(e) {}
      };
    } catch (err) {}
  }

  // Fallback Polling & Auto-Refresh for Challenges / Scoreboard
  let notifsInitialized = false;

  async function pollLiveTelemetry() {
    try {
      const urlRoot = window.init && window.init.urlRoot ? window.init.urlRoot : '';

      // 1. Check for unread notifications / First Blood
      const res = await fetch(`${urlRoot}/api/v1/notifications`, {
        headers: { 'Accept': 'application/json' }
      });
      const data = await res.json();
      if (data && data.data && Array.isArray(data.data)) {
        if (!notifsInitialized) {
          // Record current maximum ID on first run so past notifications are not replayed
          data.data.forEach(n => {
            if (n.id > lastProcessedNotifId) lastProcessedNotifId = n.id;
          });
          localStorage.setItem('cca_last_notif_id', String(lastProcessedNotifId));
          notifsInitialized = true;
        } else {
          data.data.forEach(n => {
            if (n.id > lastProcessedNotifId) {
              lastProcessedNotifId = n.id;
              localStorage.setItem('cca_last_notif_id', String(n.id));
              if (n.type === 'first_blood' || (n.title && n.title.includes('FIRST BLOOD'))) {
                showFirstBloodBanner(n);
              }
            }
          });
        }
      }

      // 2. Auto-sync Challenges if on /challenges
      if (window.location.pathname.includes('/challenges')) {
        window.dispatchEvent(new CustomEvent('load-challenges'));
      }
    } catch (e) {}
  }

  function hookCTFdEvents() {
    if (window.CTFd && window.CTFd._functions && window.CTFd._functions.events) {
      const ev = window.CTFd._functions.events;
      if (!ev._fbAttached) {
        ev._fbAttached = true;
        
        const origAlert = ev.eventAlert;
        ev.eventAlert = function(data) {
          if (data && (data.type === 'first_blood' || (data.title && data.title.includes('FIRST BLOOD')))) {
            showFirstBloodBanner(data);
            return;
          }
          if (typeof origAlert === 'function') origAlert(data);
        };

        const origToast = ev.eventToast;
        ev.eventToast = function(data) {
          if (data && (data.type === 'first_blood' || (data.title && data.title.includes('FIRST BLOOD')))) {
            showFirstBloodBanner(data);
            return;
          }
          if (typeof origToast === 'function') origToast(data);
        };
      }
    }
  }

  setInterval(patchCTFdDialogs, 250);
  setInterval(hookCTFdEvents, 300);
  setInterval(pollLiveTelemetry, 12000); // Auto-sync every 12 seconds

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      initAudioListeners();
      initDedicatedSSE();
    });
  } else {
    initAudioListeners();
    initDedicatedSSE();
  }
})();
