import scrapy

class LinkCheckerSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['https://vi.wikipedia']
    start_urls = ['https://vi.wikipedia.org/wiki/Nh%C3%A0_Ti%E1%BB%81n_L%C3%AA']

    # Add a maxdepth attribute
    maxdepth = 4

    def parse(self, response):
        # Set default meta information for first page
        from_url = ''
        from_text = ''
        depth = 0;
        # Extract the meta information from the response, if any
        if 'from' in response.meta:
            from_url = response.meta['from']
        if 'text' in response.meta:
            from_text = response.meta['text']
        if 'depth' in response.meta:
            depth = response.meta['depth']

        # Update the print logic to show what page contain a link to the
        # current page, and what was the text of the link
        print(depth, response.url, '<-', from_url, from_text, sep=' ')
        # Browse a tags only if maximum depth has not be reached
        n =1
        if depth < self.maxdepth:

            a_selectors = response.xpath("//a")
            print("len",len(a_selectors))
            for selector in a_selectors:

                text = selector.xpath("text()").extract_first()
                link = selector.xpath("@href").extract_first()
                if not link or not text or link[:6] != "/wiki/":
                    continue
                yield {
                    "link_src":from_url,
                    "link_des":"https://vi.wikipedia.org"+link,
                    "title":text,
                }


                request = response.follow(link, callback=self.parse)
                # Meta information: URL of the current page
                request.meta['from'] = response.url
                # Meta information: text of the link
                request.meta['text'] = text
                # Meta information: depth of the link
                request.meta['depth'] = depth + 1
                yield request