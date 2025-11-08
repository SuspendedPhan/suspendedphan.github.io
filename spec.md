I want a simple static website to showcase my passion project Primitive Animator. It's an IDE for motion graphics.

I want to show this screenshot and these 3 videos, which should autoplay muted and looped. There will be no other assets.

The order of importance is:
1. Screenshot
2. Videos
 - editor.mp4 - Build motion graphics with a visual expression tree. Create functions, parameters, and expressions without writing traditional code. Navigate and edit with keyboard shortcuts.
 - keyboard.mp4 - All UI elements are accessible via keyboard navigation.
 - resize.mp4 - Maximize the editor or canvas, or use a multi-pane layout.
3. Content

Here's the content:

## Features

### **Rich Built-In Functions**
Access math operations, drawing primitives (circles, rectangles), noise functions (Simplex 1D/2D), easing curves, time-based functions, and more. Compose them to create complex animations.

### **Function and Parameter System**
Organize code into reusable functions with parameters. Move functions between files, convert expressions to functions, and build a library of reusable components.

### **Multi-Project Workspace**
Manage multiple projects in one workspace. Organize code into project files and shared library files. Switch between projects quickly.

### **Keyboard-Driven Workflow**
Navigate and edit with keyboard shortcuts. Use the command palette (Cmd+K) for quick actions: create functions, navigate, convert expressions, and more.

### **Flexible Layout**
Arrange editor, canvas, and browser panes to fit your workflow. Maximize the editor or canvas, or use a multi-pane layout.

### **Powerful Drawing Primitives**
Draw shapes with position, size, color (HSV), and opacity. Use system functions like `DrawCircle` and `DrawRectangle` to build visual compositions.

### **Time-Based Animation**
Access the current time and use it to drive animations. Combine with easing functions and math operations to create smooth motion.

### **Expression Manipulation**
Move expressions in the tree, cut and paste, convert expressions to functions or parameters, and refactor code with keyboard shortcuts.

### **Project Persistence**
Projects save automatically. Export and import project data as JSON for version control and sharing.

## Architecture Overview

**Technology Stack:**
- **Domain logic**: Haskell compiled to WebAssembly via GHC-WASM
- **Expression evaluation**: Rust compiled to WebAssembly using `wasm-pack` for high-performance expression evaluation
- **Templates and styling**: React + TypeScript with Vite build system
- **Type Safety**: End-to-end type safety via auto-generated TypeScript definitions from Haskell types
- **Communication**: WASM FFI bridge between Haskell/JavaScript and Rust/JavaScript with typed message passing

**Reactive Architecture:**
- Selector-based data flow: React components subscribe to Haskell selectors via `useDh` hooks
- Action system: UI triggers actions that execute in Haskell monadic context (`AppOp`)