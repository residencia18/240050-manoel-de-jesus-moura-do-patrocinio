import { NgOptimizedImage } from '@angular/common';
import { Component } from '@angular/core';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [NgOptimizedImage],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  videoUrl: SafeResourceUrl |null= null;

  constructor(private sanitizer: DomSanitizer) { }

  ngOnInit(): void {
    // URL do vídeo do YouTube
    const youtubeVideoUrl = 'https://www.youtube.com/embed/zIDTUeZgpAg?autoplay=1&controls=0&mute=1&vq=highres';

    // Sanitize the URL
    this.videoUrl = this.sanitizer.bypassSecurityTrustResourceUrl(youtubeVideoUrl);
  }
}
