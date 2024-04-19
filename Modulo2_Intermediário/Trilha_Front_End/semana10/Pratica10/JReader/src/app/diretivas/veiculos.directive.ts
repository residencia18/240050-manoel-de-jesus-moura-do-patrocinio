import { Directive, ElementRef, OnInit, Renderer2 } from '@angular/core';

@Directive({
  selector: '[appVeiculos]',
  standalone: true
})
export class VeiculosDirective implements OnInit {

  constructor(private elemento: ElementRef, private renderizador: Renderer2) { }

  ngOnInit(): void {
    this.renderizador.setStyle(this.elemento.nativeElement, "background-color", "#2335d6")
    this.renderizador.setStyle(this.elemento.nativeElement, "color", "white")
  }
}
