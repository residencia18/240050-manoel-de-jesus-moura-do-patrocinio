export type WikipediaPage = {
    parse: {
      title: string;
      pageid: number;
      revid: number;
      text: {
        '*': string;
      };
      langlinks: {
        lang: string;
        url: string;
        langname: string;
        autonym: string;
        '*': string;
      }[];
      categories: {
        sortkey: string;
        hidden: string;
        '*': string;
      }[];
      links: {
        ns: number;
        exists: string;
        '*': string;
      }[];
      templates: {
        ns: number;
        exists: string;
        '*': string;
      }[];
      images: string[];
      externallinks: string[];
      sections: {
        toclevel: number;
        level: string;
        line: string;
        number: string;
        index: string;
        fromtitle: string;
        byteoffset: number;
        anchor: string;
        linkAnchor: string;
      }[];
      showtoc: string;
      parsewarnings: any[];
      displaytitle: string;
      iwlinks: {
        prefix: string;
        url: string;
        '*': string;
      }[];
      properties: {
        name: string;
        '*': string;
      }[];
    };
  }
  