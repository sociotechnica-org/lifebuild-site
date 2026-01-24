export interface WorkshopArticle {
  number: string;
  title: string;
  url: string;
  date: string;
}

export const workshopArticles: WorkshopArticle[] = [
  {
    number: 'WS010',
    title: 'What Happens to Your Product Org When Code Compiles Itself?',
    url: 'https://sociotechnica.org/notebook/code-compiles-itself',
    date: '2026-01-23',
  },
  {
    number: 'WS009',
    title: 'The Context Library of Alexandria (Part 1)',
    url: 'https://sociotechnica.org/notebook/context-library',
    date: '2026-01-23',
  },
  {
    number: 'WS008',
    title: 'The Year of the Software Factory',
    url: 'https://sociotechnica.org/notebook/software-factory',
    date: '2026-01-21',
  },
];

export const getRecentArticles = (count: number = 3): WorkshopArticle[] =>
  workshopArticles.slice(0, count);
