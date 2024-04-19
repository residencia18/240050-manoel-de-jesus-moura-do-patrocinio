import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { RegisterComponent } from './pages/register/register.component';
import { ProjectsComponent } from './pages/projects/projects.component';

export const routes: Routes = [
    {path: "", component:HomeComponent},
    {path: "register", component:RegisterComponent},
    {path: "projects", component:ProjectsComponent},
];
