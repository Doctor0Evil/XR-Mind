// ast.rs - ALN AST node definitions (skeleton)

#[derive(Debug)]
pub enum Node {
    Module(String),
    Struct(String),
    Datashard(String),
}
