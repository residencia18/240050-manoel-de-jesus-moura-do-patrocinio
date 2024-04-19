import { Component } from '@angular/core';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {

  ngOnInit():void{
    this.alterHeaderImg()
  }
  alterHeaderImg() {
    document.querySelector("#next")?.addEventListener("click", () => {
      const mainHeaderDiv: HTMLElement | null = window.document.getElementById("main-header");
      if (mainHeaderDiv) {
        mainHeaderDiv.style.backgroundImage = 'url("../../../assets/uesc-header-bg2.jpg")';
      }
    })
    document.querySelector("#prev")?.addEventListener("click", () => {
      const mainHeaderDiv: HTMLElement | null = window.document.getElementById("main-header");
      if (mainHeaderDiv) {
        mainHeaderDiv.style.backgroundImage = 'url("../../../assets/uesc-header-bg.webp")';
      }
    })
  }
}
