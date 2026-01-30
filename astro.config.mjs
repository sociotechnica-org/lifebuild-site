import { defineConfig } from 'astro/config';
import react from '@astrojs/react';

// Custom rehype plugin to rename "Footnotes" to "References"
function rehypeRenameFootnotes() {
  return (tree) => {
    // Find the footnotes section heading and rename it
    const visit = (node) => {
      if (node.type === 'element' && node.tagName === 'h2') {
        // Check if this is the footnotes heading (has id="footnote-label")
        if (node.properties?.id === 'footnote-label') {
          // Replace the text content
          node.children = [{ type: 'text', value: 'References' }];
        }
      }
      if (node.children) {
        node.children.forEach(visit);
      }
    };
    visit(tree);
  };
}

// https://astro.build/config
export default defineConfig({
  site: 'https://lifebuild.me',
  integrations: [react()],
  output: 'static',
  build: {
    format: 'file',
  },
  markdown: {
    rehypePlugins: [rehypeRenameFootnotes],
  },
});
