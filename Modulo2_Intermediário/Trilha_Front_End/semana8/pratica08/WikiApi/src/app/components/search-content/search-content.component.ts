import { Component, EventEmitter, Input, Output, input } from '@angular/core';
import { WikipediaPage } from '../../types/reponseWikipedia';
import { NgFor, NgIf } from '@angular/common';
import { SearchService } from '../../Services/search.service';
import { BoldTextPipe } from '../../pipes/bold-text.pipe';

@Component({
  selector: 'app-search-content',
  standalone: true,
  imports: [NgFor,NgIf, BoldTextPipe],
  templateUrl: './search-content.component.html',
  styleUrl: './search-content.component.css',

})
export class SearchContentComponent {
  @Input() pageContent: WikipediaPage | undefined  

  constructor(private wikiSearchService: SearchService) {}


  ngOnInit(): void {
    // Subscribe to the getWikiData observable

    this.wikiSearchService.getWikiData().subscribe(
      (data) => {
        this.pageContent = data;

      },
      (error) => {
        console.error('Error getting Wikipedia data:', error);
      }
    );
  }

  getFullPageLink(): string {
    return this.pageContent ? `https://en.wikipedia.org/wiki/${this.pageContent.parse.title}` : '';
  }
}
