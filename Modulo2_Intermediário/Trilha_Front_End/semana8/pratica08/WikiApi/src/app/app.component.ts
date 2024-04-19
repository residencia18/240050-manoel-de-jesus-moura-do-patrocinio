import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { SearchService } from './Services/search.service';
import { SearchInputComponent } from './components/search-input/search-input.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { SearchContentComponent } from './components/search-content/search-content.component';
import { WikipediaPage } from './types/reponseWikipedia';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet,HttpClientModule, SearchInputComponent, SearchContentComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers:[SearchService]

})
export class AppComponent {
  title = 'WikiApi';
  pageContent: any

}
