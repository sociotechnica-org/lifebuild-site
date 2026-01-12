export type ChapterStatus = 'published' | 'coming_soon';
export type ChapterPart = 'The Lens' | 'The First Win' | 'The Four Levers' | 'The Long Game';

export interface BookChapter {
  number: number;
  slug: string;
  title: string;
  part: ChapterPart;
  status: ChapterStatus;
  teaser: string;
  publish_date?: string;
  estimated_read_time?: string;
}

export const BOOK_PARTS: ChapterPart[] = [
  'The Lens',
  'The First Win',
  'The Four Levers',
  'The Long Game',
];

export const bookChapters: BookChapter[] = [
  {
    number: 1,
    slug: 'chapter-1',
    title: 'The Sovereignty Gap',
    part: 'The Lens',
    status: 'published',
    teaser:
      'Why a good life can still feel unlivable. A diagnosis of the four gaps—Balance, Restoration, Action, and Support—and the system that keeps them open.',
  },
  {
    number: 2,
    slug: 'chapter-2',
    title: 'The Taxonomy',
    part: 'The Lens',
    status: 'published',
    teaser:
      'A new way to see your life clearly. Two simple frameworks—Bronze/Silver/Gold and Red/Gray/Blue—that reveal why what matters keeps getting deferred.',
  },
  {
    number: 3,
    slug: 'chapter-3',
    title: 'Find Your Thorn',
    part: 'The First Win',
    status: 'coming_soon',
    teaser:
      'How to identify the small, recurring drain that’s quietly costing you energy every day—and why removing one thorn matters more than fixing everything.',
  },
  {
    number: 4,
    slug: 'chapter-4',
    title: 'The 72-Hour Hunt',
    part: 'The First Win',
    status: 'coming_soon',
    teaser:
      'Your first act of sovereignty. A practical, time-boxed method for eliminating, delegating, automating, or reframing a single red drain.',
  },
  {
    number: 5,
    slug: 'chapter-5',
    title: 'What You Just Built',
    part: 'The First Win',
    status: 'coming_soon',
    teaser:
      'Why that small win matters. The hidden skills you just practiced—and how they become the foundation for lasting change.',
  },
  {
    number: 6,
    slug: 'chapter-6',
    title: 'Making Your Life Visible',
    part: 'The Four Levers',
    status: 'coming_soon',
    teaser:
      'When you can see what you’re carrying, you can choose what to put down. How visibility closes the Balance gap.',
  },
  {
    number: 7,
    slug: 'chapter-7',
    title: 'Building Your Support Team',
    part: 'The Four Levers',
    status: 'coming_soon',
    teaser:
      'Why carrying everything alone is optional—and how to distribute the load without guilt or friction.',
  },
  {
    number: 8,
    slug: 'chapter-8',
    title: 'Protecting Your Capacity',
    part: 'The Four Levers',
    status: 'coming_soon',
    teaser:
      'How to stop depletion from being the default. Managing energy as a resource, not a mystery.',
  },
  {
    number: 9,
    slug: 'chapter-9',
    title: 'Working Your System',
    part: 'The Four Levers',
    status: 'coming_soon',
    teaser:
      'Turning effort into momentum. How rhythms, limits, and reviews close the Action gap and make progress compound.',
  },
  {
    number: 10,
    slug: 'chapter-10',
    title: 'What Sovereignty Looks Like',
    part: 'The Long Game',
    status: 'coming_soon',
    teaser:
      'The integrated picture. What changes when visibility, support, capacity, and systems work together.',
  },
  {
    number: 11,
    slug: 'chapter-11',
    title: 'Where to Go From Here',
    part: 'The Long Game',
    status: 'coming_soon',
    teaser:
      'Three paths forward—stop here, build light systems, or go deeper—and how to choose what fits your life.',
  },
];
