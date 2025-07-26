Automatizované testy pro web Exim Tours

Tento projekt obsahuje 3 základní automatizované testy webu www.eximtours.cz napsané pomocí frameworku Playwright v  Pythonu.

Pro každý test se otevře okno prohlížeče (Chromium), které simuluje chování uživatele. Okno je zvětšené na full screen 1920×1080, aby byl test vizuálně přehledný. Díky parametru slow_mo=500 jsou všechny akce zpomaleny o 500 ms a je tak možné dobře sledovat každý krok. Pokud se zobrazí cookie lišta, je automaticky potvrzena (max. do 2 sekund). Pokud se nezobrazí, test pokračuje dál bez chyby.

Spuštění testů probíhá v terminálu zadáním příkazu "pytest test_engeto_playwright.py". Pro podrobnější výpis se použije příkaz "pytest test_engeto_playwright.py -v". 

TC:
test_main_menu_visible
Ověří, že hlavní menu je po načtení stránky viditelné

test_title_eximtours
Ověří, že titulek stránky obsahuje text "EXIM tours"

test_click_on_pardubice
Klikne na odkaz „Pardubice“ a ověří, že přesměrování na stránku s odlety z Pardubic proběhlo správně.
