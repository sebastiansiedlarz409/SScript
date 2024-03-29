from enum import Enum

class SSTokens(Enum):
    LetKwToken = 0,
    ConstKwToken = 1,
    FuncKwToken = 2,
    ReturnKwToken = 3,
    IfKwToken = 4,
    ElifKwToken = 5,
    ElseKwToken = 6,
    ForKwToken = 7,
    WhileKwToken = 8,
    DoKwToken = 9,
    BreakKwToken = 10,
    ContinueKwToken = 11,
    AndKwToken = 12,
    OrKwToken = 13,
    EqKwToken = 14,
    NeqKwToken = 15,
    GrKwToken = 16,
    GeKwToken = 17,
    LsKwToken = 18,
    LeKwToken = 19,
    NullKwToken = 20,
    TrueKwToken = 21,
    FalseKwToken = 22,
    StructKwToken = 23,
    ImplKwToken = 24,
    AccessModifierKwToken = 25,
    AllocKwToken = 26,
    SelfKwToken = 27,
    IdentifierToken = 30,
    NumberToken = 31,
    StringToken = 32,
    AssignOperatorToken = 40,
    UnaryOperatorToken = 41,
    BinaryOperatorToken = 42,
    PrefixOperatorToken = 43,
    CommaToken = 51,
    ColonToken = 52,
    SemicolonToken = 53,
    DotToken = 54,
    LParenToken = 60,
    RParenToken = 61,
    LBracketToken = 62, #{}
    RBracketToken = 63,
    LSquareBracketToken = 64, #[]
    RSquareBracketToken = 65,
    QuoteToken = 66,
    LogKwToken = 8000,
    LoglnKwToken = 8001,
    EOFToken = 9000

SSKEYWORDS = {
    "log" : SSTokens.LogKwToken,
    "logln" : SSTokens.LoglnKwToken,
    "let" : SSTokens.LetKwToken,
    "const": SSTokens.ConstKwToken,
    "func": SSTokens.FuncKwToken,
    "return": SSTokens.ReturnKwToken,
    "if": SSTokens.IfKwToken,
    "elif": SSTokens.ElifKwToken,
    "else": SSTokens.ElseKwToken,
    "for": SSTokens.ForKwToken,
    "while": SSTokens.WhileKwToken,
    "do": SSTokens.DoKwToken,
    "break": SSTokens.BreakKwToken,
    "continue": SSTokens.ContinueKwToken,
    "and": SSTokens.AndKwToken,
    "or": SSTokens.OrKwToken,
    "not": SSTokens.UnaryOperatorToken,
    "eq": SSTokens.EqKwToken,
    "neq": SSTokens.NeqKwToken,
    "gr": SSTokens.GrKwToken,
    "ge": SSTokens.GeKwToken,
    "ls": SSTokens.LsKwToken,
    "le": SSTokens.LeKwToken,
    "true": SSTokens.TrueKwToken,
    "false": SSTokens.FalseKwToken,
    "null": SSTokens.NullKwToken,
    "struct": SSTokens.StructKwToken,
    "public": SSTokens.AccessModifierKwToken,
    "private": SSTokens.AccessModifierKwToken,
    "impl": SSTokens.ImplKwToken,
    "alloc": SSTokens.AllocKwToken,
    "self": SSTokens.SelfKwToken
}