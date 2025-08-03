const categorySelector = document.getElementById('category');
const container = document.getElementById('news-container');

async function fetchNews(category = 'general') {
  const res = await fetch(`http://localhost:5000/news?category=${category}`);
  const data = await res.json();
  container.innerHTML = '';
  data.articles.forEach(article => {
    const div = document.createElement('div');
    div.className = 'article';
    div.innerHTML = `
      <img src="${article.urlToImage || ''}" />
      <h2>${article.title}</h2>
      <p>${article.description || ''}</p>
      <a href="${article.url}" target="_blank">Read More</a>
    `;
    container.appendChild(div);
  });
}

categorySelector.addEventListener('change', (e) => {
  fetchNews(e.target.value);
});

window.onload = () => fetchNews();
