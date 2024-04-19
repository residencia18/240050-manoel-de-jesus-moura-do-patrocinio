import { Directive, ElementRef, OnInit, Renderer2 } from '@angular/core';

@Directive({
  selector: '[appCategorias]',
  standalone: true
})
export class CategoriasDirective implements OnInit {

  constructor(private elemento: ElementRef, private renderizador: Renderer2) { }

  ngOnInit(): void {
    this.renderizador.setStyle(this.elemento.nativeElement, "background-color", "#663399")
    this.renderizador.setStyle(this.elemento.nativeElement, "color", "white")
  }

}
