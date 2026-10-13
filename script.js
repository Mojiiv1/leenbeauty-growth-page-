// Language switching only. All navigation is handled by ordinary links.
const copy = {
  en: {
    skip: 'Skip to content', eyebrow: 'Ottawa · Hemlock Road',
    headline: 'Elegance in <em>every detail.</em>',
    intro: 'Precision cuts, beautiful colour and expert beauty care. Book, explore and connect in one place.',
    directions: 'Directions', bookTitle: 'Book an Appointment',
    bookNote: 'Choose your service and a time that works for you',
    reviewTitle: 'Google Reviews', reviewNote: 'See our reviews and share your experience',
    quickTitle: 'Explore & connect', call: 'Call Salon', official: 'Official Website',
    storyEyebrow: 'Recent work', storyTitle: 'Beautiful hair.<br><em>Beautiful moments.</em>',
    storyText: 'A glimpse of the styles created at Leen Beauty Centre. See more inspiration on Instagram.',
    viewInstagram: 'View more on Instagram ↗', noteTitle: 'All your beauty links. One tap.',
    noteText: 'Book, connect and explore in one simple place.'
  },
  fr: {
    skip: 'Aller au contenu', eyebrow: 'Ottawa · chemin Hemlock',
    headline: 'L’élégance dans <em>les moindres détails.</em>',
    intro: 'Coiffure et soins de beauté avec une attention personnalisée. Tous vos liens sont ici.',
    directions: 'Itinéraire', bookTitle: 'Prendre rendez-vous',
    bookNote: 'Choisissez le service et l’heure qui vous conviennent',
    reviewTitle: 'Avis Google', reviewNote: 'Consultez les avis et partagez votre expérience',
    quickTitle: 'Explorer et communiquer', call: 'Appeler le salon', official: 'Site officiel',
    storyEyebrow: 'Nos réalisations', storyTitle: 'De beaux cheveux.<br><em>De beaux moments.</em>',
    storyText: 'Un aperçu des coiffures réalisées chez Leen Beauty Centre. Trouvez d’autres idées sur Instagram.',
    viewInstagram: 'Voir plus sur Instagram ↗', noteTitle: 'Tous vos liens beauté. Un seul clic.',
    noteText: 'Réservez, explorez et communiquez au même endroit.'
  }
};
function setLanguage(language) {
  const lang = copy[language] ? language : 'en';
  document.documentElement.lang = lang;
  for (const node of document.querySelectorAll('[data-i18n]')) {
    const value = copy[lang][node.dataset.i18n];
    if (value) node.textContent = value;
  }
  for (const node of document.querySelectorAll('[data-i18n-html]')) {
    const value = copy[lang][node.dataset.i18nHtml];
    if (value) node.innerHTML = value;
  }
  for (const button of document.querySelectorAll('[data-lang]')) {
    button.setAttribute('aria-pressed', String(button.dataset.lang === lang));
  }
  try { localStorage.setItem('leen-growth-language', lang); } catch (_) {}
}
for (const button of document.querySelectorAll('[data-lang]')) {
  button.addEventListener('click', () => setLanguage(button.dataset.lang));
}
let language = 'en';
try { language = localStorage.getItem('leen-growth-language') || 'en'; } catch (_) {}
setLanguage(language);
