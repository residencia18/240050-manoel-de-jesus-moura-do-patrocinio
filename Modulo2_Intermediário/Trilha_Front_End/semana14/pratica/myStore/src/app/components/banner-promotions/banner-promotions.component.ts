import { Component } from '@angular/core';

@Component({
  selector: 'app-banner-promotions',
  standalone: true,
  imports: [],
  templateUrl: './banner-promotions.component.html',
  styleUrl: './banner-promotions.component.css'
})
export class BannerPromotionsComponent {
  ngOnInit():void{
    this.alterHeaderImg()
  }
  alterHeaderImg() {
    document.querySelector("#next")?.addEventListener("click", () => {
      const mainHeaderDiv: HTMLElement | null = window.document.getElementById("main-header");
      if (mainHeaderDiv) {
        mainHeaderDiv.style.backgroundImage = 'url("../../../assets/banner2.jpg")';
      }
    })
    document.querySelector("#prev")?.addEventListener("click", () => {
      const mainHeaderDiv: HTMLElement | null = window.document.getElementById("main-header");
      if (mainHeaderDiv) {
        mainHeaderDiv.style.backgroundImage = 'url("../../../assets/banner1.jpg")';
      }
    })
  }
}
