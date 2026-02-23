// (function(){
//   // Minimal listener-only script for homepage CTA buttons
//   function init(){
//     const historyBtn = document.querySelector('.cta-buttons a[href="/history"]');
//     const chatBtn = document.querySelector('.cta-buttons a[href="/chat"]');

//     if(historyBtn){
//       historyBtn.addEventListener('click', function(){
//         window.dispatchEvent(new CustomEvent('homepage:ctaClick', { detail: { target: 'history' } }));
//         console.log('[CareMap] CTA clicked: history');
//       });
//     }

//     if(chatBtn){
//       chatBtn.addEventListener('click', function(){
//         window.dispatchEvent(new CustomEvent('homepage:ctaClick', { detail: { target: 'chat' } }));
//         console.log('[CareMap] CTA clicked: chat');
//       });
//     }
//   }

//   document.addEventListener('DOMContentLoaded', init);
// })();
