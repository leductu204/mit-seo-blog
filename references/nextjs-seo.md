# Next.js SEO Patterns (App Router)

## generateMetadata per slug

```typescript
// app/blog/[slug]/page.tsx
import { Metadata } from 'next'
import { getPostBySlug } from '@/lib/blog'
import { notFound } from 'next/navigation'

export async function generateMetadata({ params }: { params: { slug: string } }): Promise<Metadata> {
  const post = await getPostBySlug(params.slug)
  if (!post) return {}

  return {
    title: post.meta_title || `${post.title} | Tram Sang Tao`,
    description: post.meta_description || post.description,
    openGraph: {
      title: post.title,
      description: post.description,
      images: post.cover_image ? [{ url: post.cover_image }] : [],
      type: 'article',
      publishedTime: post.published_at,
    },
    alternates: {
      canonical: `https://tramsangtao.com/blog/${post.slug}`,
    },
  }
}
```

## JSON-LD Article Schema

```typescript
// components/BlogJsonLd.tsx
export function BlogJsonLd({ post }: { post: BlogPost }) {
  const schema = {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: post.title,
    description: post.description,
    image: post.cover_image,
    datePublished: post.published_at,
    dateModified: post.updated_at,
    author: { '@type': 'Organization', name: 'Tram Sang Tao' },
    publisher: {
      '@type': 'Organization',
      name: 'Tram Sang Tao',
      url: 'https://tramsangtao.com',
    },
  }

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }}
    />
  )
}
```

## sitemap.ts

```typescript
// app/sitemap.ts
import { MetadataRoute } from 'next'
import { getAllPublishedSlugs } from '@/lib/blog'

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const posts = await getAllPublishedSlugs()

  const blogEntries = posts.map((post) => ({
    url: `https://tramsangtao.com/blog/${post.slug}`,
    lastModified: post.updated_at,
    changeFrequency: 'weekly' as const,
    priority: 0.7,
  }))

  return [
    { url: 'https://tramsangtao.com', changeFrequency: 'daily', priority: 1 },
    { url: 'https://tramsangtao.com/pricing', changeFrequency: 'weekly', priority: 0.9 },
    { url: 'https://tramsangtao.com/blog', changeFrequency: 'daily', priority: 0.8 },
    ...blogEntries,
  ]
}
```

## robots.ts

```typescript
// app/robots.ts
import { MetadataRoute } from 'next'

export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: '*',
      allow: '/',
      disallow: ['/api/', '/admin/'],
    },
    sitemap: 'https://tramsangtao.com/sitemap.xml',
  }
}
```

## ISR for blog post pages

```typescript
// Revalidate every hour
export const revalidate = 3600

// Or on-demand via route handler
// POST /api/revalidate?secret=xxx&slug=huong-dan-kling
```
