template = '''<html lang="ru"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ожидание сигнала</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Courier New', monospace;
            background: #0a0a0a;
            color: #00ff00;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .container {
            text-align: center;
            padding: 40px;
            border: 2px solid #0f0;
            border-radius: 8px;
            background: #000;
            max-width: 600px;
            width: 90%;
        }

        .dot {
            display: inline-block;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #0f0;
            animation: pulse 0.8s infinite;
            margin-right: 8px;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; box-shadow: 0 0 8px #0f0; }
            50% { opacity: 0.2; box-shadow: 0 0 1px #0f0; }
        }

        .message-box {
            margin: 30px 0;
            padding: 30px;
            border: 2px dashed #0f0;
            border-radius: 5px;
            min-height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.6rem;
            word-break: break-all;
            transition: 0.2s;
        }

        .message-box.got-it {
            border: 3px solid #ff0;
            border-style: solid;
            background: #111100;
            animation: grab 0.2s ease-out;
        }

        @keyframes grab {
            0% { transform: scale(1.1); border-color: #fff; }
            100% { transform: scale(1); border-color: #ff0; }
        }

        .sub {
            font-size: 0.65rem;
            opacity: 0.4;
            margin-top: 15px;
        }
    </style>
<style>
      body.shimeji-pinned iframe {
        pointer-events: none;
      }
      body.shimeji-select-ie {
        cursor: cell !important;
      }
      #shimeji-contextMenu::-webkit-scrollbar {
        width: 6px;
      }
      #shimeji-contextMenu::-webkit-scrollbar-thumb {
        background-color: rgba(30,30,30,0.6);
        border-radius: 3px;
      }
      #shimeji-contextMenu::-webkit-scrollbar-thumb:hover {
        background: #555;
      }
    </style><meta name="shimejiBrowserExtensionId" content="gohjpllcolmccldfdggmamodembldgpc" data-version="2.0.5"><style type="text/css">
.vfm--fixed[data-v-2836fdb5] {
  position: fixed;
}
.vfm--absolute[data-v-2836fdb5] {
  position: absolute;
}
.vfm--inset[data-v-2836fdb5] {
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
.vfm--overlay[data-v-2836fdb5] {
  background-color: rgba(0, 0, 0, 0.5);
}
.vfm--prevent-none[data-v-2836fdb5] {
  pointer-events: none;
}
.vfm--prevent-auto[data-v-2836fdb5] {
  pointer-events: auto;
}
.vfm--outline-none[data-v-2836fdb5]:focus {
  outline: none;
}
.vfm-enter-active[data-v-2836fdb5],
.vfm-leave-active[data-v-2836fdb5] {
  transition: opacity 0.2s;
}
.vfm-enter-from[data-v-2836fdb5],
.vfm-leave-to[data-v-2836fdb5] {
  opacity: 0;
}
.vfm--touch-none[data-v-2836fdb5] {
  touch-action: none;
}
.vfm--select-none[data-v-2836fdb5] {
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
}
.vfm--resize-tr[data-v-2836fdb5],
.vfm--resize-br[data-v-2836fdb5],
.vfm--resize-bl[data-v-2836fdb5],
.vfm--resize-tl[data-v-2836fdb5] {
  width: 12px;
  height: 12px;
  z-index: 10;
}
.vfm--resize-t[data-v-2836fdb5] {
  top: -6px;
  left: 0;
  width: 100%;
  height: 12px;
  cursor: ns-resize;
}
.vfm--resize-tr[data-v-2836fdb5] {
  top: -6px;
  right: -6px;
  cursor: nesw-resize;
}
.vfm--resize-r[data-v-2836fdb5] {
  top: 0;
  right: -6px;
  width: 12px;
  height: 100%;
  cursor: ew-resize;
}
.vfm--resize-br[data-v-2836fdb5] {
  bottom: -6px;
  right: -6px;
  cursor: nwse-resize;
}
.vfm--resize-b[data-v-2836fdb5] {
  bottom: -6px;
  left: 0;
  width: 100%;
  height: 12px;
  cursor: ns-resize;
}
.vfm--resize-bl[data-v-2836fdb5] {
  bottom: -6px;
  left: -6px;
  cursor: nesw-resize;
}
.vfm--resize-l[data-v-2836fdb5] {
  top: 0;
  left: -6px;
  width: 12px;
  height: 100%;
  cursor: ew-resize;
}
.vfm--resize-tl[data-v-2836fdb5] {
  top: -6px;
  left: -6px;
  cursor: nwse-resize;
}
</style><style type="text/css">x-vue-echarts{display:block;width:100%;height:100%;min-width:0}
</style><link rel="stylesheet" href="chrome-extension://lkhiljgmbeecmljiogckofcalncmfnfo/assets/browser.css"><link rel="preconnect" href="https://migaku-public-data.migaku.com" crossorigin="anonymous"><link rel="preload" href="https://migaku-public-data.migaku.com/fonts/inter/InterVariable.woff2?v=4.0" as="font" type="font/woff" crossorigin="anonymous"><link rel="preload" href="https://migaku-public-data.migaku.com/fonts/gt-maru/GT-Maru-Black.woff2" as="font" type="font/woff" crossorigin="anonymous"></head>
<body><div id="MigakuShadowDom" data-mgk-ready="false" data-mgk-lang-selected="" data-mgk-interface-lang="en" data-mgk-app-open="false"></div>
    <div class="container">
        <h1><span class="dot"></span> МОНИТОРИНГ</h1>
        <p style="opacity:0.5; font-size:0.8rem; margin-top:5px;">
            Новое сообщение заменяет предыдущее
        </p>

        <div class="message-box" id="msgBox">
            <span id="msgText" style="opacity: 0.35;">ожидание...</span>
        </div>

        <div class="sub">
            запросов: <span id="cnt">3260</span> |
            опрос каждые 300 мс
        </div>
    </div>

    <script>
        const box = document.getElementById('msgBox');
        const text = document.getElementById('msgText');
        const cnt = document.getElementById('cnt');

        let n = 0;
        let hadMessage = false;

        async function poll() {
            try {
                n++;
                cnt.textContent = n;

                hadMessage = true;
                text.textContent = "~~~";
                text.style.opacity = '1';
                box.classList.add('got-it');
                
                try {
                    const a = new (window.AudioContext || window.webkitAudioContext)();
                    const o = a.createOscillator();
                    const g = a.createGain();
                    o.connect(g); g.connect(a.destination);
                    o.frequency.value = 250;
                    g.gain.value = 1;
                    o.start(); o.stop(a.currentTime + 1.2);
                } catch(e) {}

                setTimeout(() => box.classList.remove('got-it'), 1200);
                text.textContent = "waiting...";
                setTimeout(() => console.log(""), 2300);
                text.textContent = "~~~";
                    

            } catch(e) {
                text.textContent = 'нет связи';
                text.style.opacity = '0.5';
            }
        }
        
        async function wait(){
            
        }

        setInterval(poll, 3500);
        poll();
    </script>

<div id="shimeji-workArea" style="position: fixed; background: transparent; z-index: 2147483643; width: 100vw; height: 100vh; left: 0px; top: 0px; transform: translate(0px, 0px); pointer-events: none;"></div></body></html>'''

