import { Component, EventEmitter, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { SearchService } from '../../Services/search.service';
import { NgFor, NgIf } from '@angular/common';
import { WikipediaPage } from '../../types/reponseWikipedia';

@Component({
  selector: 'app-search-input',
  standalone: true,
  imports: [FormsModule,NgIf,NgFor],
  templateUrl: './search-input.component.html',
  styleUrl: './search-input.component.css'
})
export class SearchInputComponent {
  searchTitle = '';
  pageContent: WikipediaPage | undefined
  @Output() resultSearch = new EventEmitter<WikipediaPage>();

  constructor(private wikiSearchService: SearchService) {}

  search(): void {
    this.wikiSearchService.search(this.searchTitle).subscribe(
      (data:any) => {
        this.pageContent = JSON.parse(data) as WikipediaPage;
        this.wikiSearchService.setRearchData(this.pageContent)
        this.resultSearch.emit(this.pageContent);

      },
      (error) => {
        console.error('Error getting Wikipedia data:', error);
      }
    );
  }

  
}
