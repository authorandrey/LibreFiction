document.addEventListener('DOMContentLoaded', function() {
    const chapterContent = document.getElementById('chapter-content');
    if (!chapterContent) return;

    const fontIncrease = document.getElementById('font-increase');
    const fontDecrease = document.getElementById('font-decrease');
    const fontSerif = document.getElementById('font-serif');
    const fontSans = document.getElementById('font-sans');
    const scrollUp = document.getElementById('scroll-up');
    const scrollDown = document.getElementById('scroll-down');

    function applyStoredStyles() {
        const storedFontSize = localStorage.getItem('chapterFontSize');
        const storedFontFamily = localStorage.getItem('chapterFontFamily');
        if (storedFontSize) {
            chapterContent.style.fontSize = storedFontSize;
        }
        if (storedFontFamily) {
            chapterContent.style.fontFamily = storedFontFamily;
        }
    }

    applyStoredStyles();

    let currentFontSize = parseFloat(getComputedStyle(chapterContent).fontSize);
    const step = 2;

    fontIncrease?.addEventListener('click', () => {
        if (currentFontSize < 30) {
            currentFontSize += step;
            chapterContent.style.fontSize = currentFontSize + 'px';
            localStorage.setItem('chapterFontSize', currentFontSize + 'px');
        }
    });

    fontDecrease?.addEventListener('click', () => {
        if (currentFontSize > 12) {
            currentFontSize -= step;
            chapterContent.style.fontSize = currentFontSize + 'px';
            localStorage.setItem('chapterFontSize', currentFontSize + 'px');
        }
    });

    fontSerif?.addEventListener('click', () => {
        const serifFamily = 'Georgia, "Times New Roman", Times, serif';
        chapterContent.style.fontFamily = serifFamily;
        localStorage.setItem('chapterFontFamily', serifFamily);
    });

    fontSans?.addEventListener('click', () => {
        const sansFamily = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif';
        chapterContent.style.fontFamily = sansFamily;
        localStorage.setItem('chapterFontFamily', sansFamily);
    });

    scrollUp?.addEventListener('click', () => {
        window.scrollTo({ top:0, behavior: 'smooth'});
    });

    scrollDown?.addEventListener('click', () => {
        window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth'});
    });
});