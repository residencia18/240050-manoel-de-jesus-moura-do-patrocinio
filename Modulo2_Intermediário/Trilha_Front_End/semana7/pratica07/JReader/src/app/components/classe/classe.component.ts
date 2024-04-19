import { Component, EventEmitter, Input, Output } from '@angular/core';
import { NgFor } from '@angular/common';
import { CategoriasDirective } from '../../diretivas/categorias.directive';

@Component({
  selector: 'app-classe',
  standalone: true,
  imports: [NgFor,CategoriasDirective],
  templateUrl: './classe.component.html',
  styleUrl: './classe.component.css'
})
export class ClasseComponent {
  @Input() categorias: any
  @Output() categoriaEscolhida = new EventEmitter<{ categoria: string, items: [] }>();

  obterChaves(): string[] {
    return this.categorias ? Object.keys(this.categorias) : [];
  }


  selectCategoria(categoria: string) {
    this.categoriaEscolhida.emit({ categoria, items: this.categorias[categoria] });
  }
}
